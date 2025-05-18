### Now, let's add an equation using json_equationer ###
import json_equationer
Arrhenius_equation_example = json_equationer.equation_creator.Equation()
Arrhenius_equation_example.set_x_variable("T (K)")  # Temperature in Kelvin
Arrhenius_equation_example.set_y_variable("k (s**-1)")  # Rate constant in inverse seconds
Arrhenius_equation_example.set_equation("k = A * (e ** (-Ea / (R * T)))")
# Add constants one at a time, or through a list. We'll use a different Ea for this one.
Arrhenius_equation_example.add_constants({"Ea": "40000 J/mol"})  
Arrhenius_equation_example.add_constants([
    {"R": "8.314 J/(mol*K)"},
    {"A": "1*10**13 (s**-1)"},
    {"e": "2.71828"}  # No unit required
])
# Optinally, set minimum number of points and limits for calculations.
Arrhenius_equation_example.set_num_of_points(10)
Arrhenius_equation_example.set_x_range_default([200, 500])
Arrhenius_equation_example.set_x_range_limits([None, 600])  

# Define additional properties.
Arrhenius_equation_example.equation_dict["points_spacing"] = "Linear"


Arrhenius_equation_example.print_equation_dict()