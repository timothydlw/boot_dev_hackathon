#activity multipliers
sedentary = 1.2
lightly_active = 1.375
moderately_active = 1.550
very_active = 1.725
extra_active = 1.9

#goal modifiers
weight_loss = 0.9 #10% reduction
weight_maintenance = 1 #no change
weight_gain = 500 #500 calorie surplus

#input conversions
def convert_to_kg(weight):
    return weight / 2.205  # pounds to kg
def convert_to_cm(feet, inches):
    return (feet * 12 + inches) * 2.54  # feet and inches to cm

#macronutrient conversions
protein_per_kg = 1.65  # grams of protein per kg of body weight
protein_per_lb = 0.75  # grams of protein per lb of body weight

fats_per_lb = 0.5  # grams of fats per lb of body weight
fats_per_kg = 1.1  # grams of fats per kg of body weight