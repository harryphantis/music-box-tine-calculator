# Music box tine calculator
# Calculates tine lengths from L = sqrt(0.162 * t * sqrt(E / rho) / f)
# and compares them with hand-calculated values. All units are SI.

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


# Temporary test: one note (A4, 440 Hz) in brass
brass = materials["brass_1mm_cm"]
print(tine_length(440, brass["E"], brass["rho"], brass["t"]) * 100, "cm")
