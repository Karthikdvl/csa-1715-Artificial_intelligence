% Facts: Define disease-diet relationships
disease(diabetes, low_carb_diet).
disease(hypertension, low_salt_diet).
disease(heart_disease, low_fat_diet).
disease(gout, low_purine_diet).

% Rule: Suggest diet based on disease
suggest_diet(Disease, Diet) :-
    disease(Disease, Diet).

% Example queries:
% 1. Query: suggest_diet(diabetes, Diet).
%    Result: Diet = low_carb_diet

% 2. Query: suggest_diet(heart_disease, Diet).
%    Result: Diet = low_fat_diet
