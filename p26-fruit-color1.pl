% Facts about fruit colors
colour(cherry, red).
colour(banana, yellow).
colour(apple, red).
colour(apple, green).
colour(orange, orange).

% Rule to find the color of a fruit
fruit_color(Fruit, Color) :- colour(Fruit, Color).

% Example queries
% Query: fruit_color(cherry, Color).
% Output: red
