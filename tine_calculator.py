# Music box tine calculator
# Calculates tine lengths from L = sqrt(0.162 * t * sqrt(E / rho) / f)
# and compares them with hand-calculated values. All units are SI.

import csv
import math

# Material properties. Keys match the column names in the CSV.
materials = {
    "brass_1mm_cm": {
        "E": 110e9,     # 110 GPa in Pa
        "rho": 8530,    # 8.53 g/cm³ in kg/m³
        "t": 0.001,     # 1 mm in m
    },
    "spring_steel_1mm_cm": {
        "E": 190e9,     # 190 GPa in Pa
        "rho": 7850,    # 7.85 g/cm³ in kg/m³ (value used in hand calculations)
        "t": 0.001,     # 1 mm in m
    },
    "pmma_3mm_cm": {
        "E": 2.77e9,    # 2.77 GPa in Pa
        "rho": 1190,    # 1.19 g/cm³ in kg/m³
        "t": 0.003,     # 3 mm in m
    },
}


def tine_length(frequency, youngs_modulus, density, thickness):
    wave_speed = math.sqrt(youngs_modulus / density)
    length = math.sqrt(0.162 * thickness * wave_speed / frequency)
    return length


# Calculate every note in every material, compare with the hand values
# and save one row per note and material to the results file.
# Only runs when this file is run directly, not when another file imports it.
if __name__ == "__main__":
    with open("tine_lengths_report_table.csv") as file, open("tine_lengths_results.csv", "w", newline="") as results_file:
        reader = csv.DictReader(file)
        writer = csv.writer(results_file)
        writer.writerow(["note", "frequency_hz", "material", "hand_cm", "calculated_cm", "percent_difference"])
        for row in reader:
            frequency = float(row["frequency_hz"])
            for material_name, properties in materials.items():
                hand_cm = float(row[material_name])
                calculated_cm = tine_length(frequency, properties["E"], properties["rho"], properties["t"]) * 100
                percent_difference = (calculated_cm - hand_cm) / hand_cm * 100
                writer.writerow([row["note"], frequency, material_name, hand_cm, round(calculated_cm, 2), round(percent_difference, 2)])
    print("Saved results to tine_lengths_results.csv")
