import tkinter as tk
from tkinter import ttk
import math

# CALC FUNCTIONS
def calculate_force(mass, acceleration):
    return mass * acceleration

def calculate_work(force, distance):
    return force * distance

def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def calculate_potential_energy(mass, height, gravity=9.81):
    return mass * gravity * height

def calculate_projectile_range(velocity, angle, gravity=9.81):
    angle_rad = math.radians(angle)
    return (velocity ** 2 * math.sin(2 * angle_rad)) / gravity

# DROP DOWN HEADERS
calculations = {
    "Force (F = m * a)": ("mass", "acceleration"),
    "Work (W = F * d)": ("force", "distance"),
    "Kinetic Energy (KE = 0.5 * m * v^2)": ("mass", "velocity"),
    "Potential Energy (PE = m * g * h)": ("mass", "height"),
    "Projectile Range": ("velocity", "angle")
}

# MAIN CALC FUNCTION IN GUI USING STARGUMENTS FOR INPUTS
def perform_calculation():
    try:
        calc_type = calc_selection.get()
        inputs = [float(entry_fields[var].get()) for var in calculations[calc_type]]
        
        if calc_type == "Force (F = m * a)":
            result = calculate_force(*inputs)
        elif calc_type == "Work (W = F * d)":
            result = calculate_work(*inputs)
        elif calc_type == "Kinetic Energy (KE = 0.5 * m * v^2)":
            result = calculate_kinetic_energy(*inputs)
        elif calc_type == "Potential Energy (PE = m * g * h)":
            result = calculate_potential_energy(*inputs)
        elif calc_type == "Projectile Range":
            result = calculate_projectile_range(*inputs)
        
        result_label.config(text=f"Result: {result:.2f}")
    except Exception as e:
        result_label.config(text="Error in calculation.")

# TKINTER
root = tk.Tk()
root.title("PHYSICS CALC NEW GUI")
root.geometry("360x300")
root.configure(bg='black')

# COMBOBOX DROPDOWN

style = ttk.Style(root)
style.theme_use('clam')
style.configure("TCombobox",
                fieldbackground="black",
                background="black",
                foreground="black",  
                arrowcolor="white")

calc_selection = ttk.Combobox(root, values=list(calculations.keys()), state="readonly", font=("Mono", 14))
calc_selection.grid(row=0, column=0, columnspan=2, padx=20, pady=15)
calc_selection.set("Select Calculation")

# ENTRY FIELDS
entry_fields = {}

# UPDATE FIELDS BSED ON INPUT
def update_fields(event):
    # CLEAR
    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) > 0:
            widget.grid_remove()
    
    calc_type = calc_selection.get()
    for row, var_name in enumerate(calculations[calc_type], start=1):
        tk.Label(root, text=f"{var_name.capitalize()}:", font=("Mono", 14), bg="black", fg="white").grid(
            row=row, column=0, sticky="e", padx=10, pady=5
        )
        
        entry = tk.Entry(root, font=("Mono", 14), relief="solid", borderwidth=1)
        entry_fields[var_name] = entry
        entry.grid(row=row, column=1, padx=10, pady=5)
    
    # REPOSITION CALC AND RESULT
    calculate_button.grid(row=row+1, column=0, columnspan=2, pady=20)
    result_label.grid(row=row+2, column=0, columnspan=2)

calc_selection.bind("<<ComboboxSelected>>", update_fields)

# CALC BUTTON STYLING
calculate_button = tk.Button(
    root, text="Calculate", command=perform_calculation,
    font=("Mono", 14, "bold"), bg="black", fg="black", relief="raised", padx=10, pady=5
)
calculate_button.grid(row=6, column=0, columnspan=2, pady=20)

# RESULT STYLING
result_label = tk.Label(
    root, text="Result:", font=("Mono", 14, "bold"), fg="white", bg="black"
)
result_label.grid(row=7, column=0, columnspan=2)


root.mainloop()
