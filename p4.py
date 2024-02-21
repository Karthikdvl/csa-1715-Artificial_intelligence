from ortools.sat.python import cp_model

def solve_cryptarithmetic():
    model = cp_model.CpModel()

    # Define the variables
    base = 10
    letters = ['C', 'P', 'I', 'S', 'F', 'U', 'N', 'T', 'R', 'E']
    variables = {letter: model.NewIntVar(0, 9, letter) for letter in letters}

    # Add constraints
    model.AddAllDifferent(variables.values())
    model.Add(variables['C'] * 10 + variables['P'] + variables['I'] * 10 + variables['S']
              + variables['F'] * base**2 + variables['U'] * 10 + variables['N']
              == variables['T'] * 10**3 + variables['R'] * 10**2 + variables['U'] * 10 + variables['E'])

    # Create a solution printer
    class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
        def __init__(self, variables):
            cp_model.CpSolverSolutionCallback.__init__(self)
            self.variables = variables
            self.solution_count = 0

        def on_solution_callback(self):
            self.solution_count += 1
            for v in self.variables:
                print(f"{v} = {self.Value(self.variables[v])}", end=' ')
            print()

    # Solve the problem
    solver = cp_model.CpSolver()
    solution_printer = VarArraySolutionPrinter(variables)
    status = solver.SearchForAllSolutions(model, solution_printer)

    if solution_printer.solution_count == 0:
        print("No solution found.")

solve_cryptarithmetic()
