# Works backwards from the hand-calculated lengths to find the material
# properties that would have produced them.
# L is proportional to sqrt(t) * (E / rho) ** 0.25, so if the hand length is
# r times the calculated length, the hand E/rho was r**4 times bigger
# and the hand t was r**2 times bigger.

import csv
from tine_calculator import tine_length, materials

for material_name, properties in materials.items():
    # Ratio of hand length to calculated length for each of the 16 notes
    ratios = []
    with open("tine_lengths_report_table.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            frequency = float(row["frequency_hz"])
            hand_cm = float(row[material_name])
            calculated_cm = tine_length(frequency, properties["E"], properties["rho"], properties["t"]) * 100
            ratios.append(hand_cm / calculated_cm)
    r = sum(ratios) / len(ratios)

    implied_E = properties["E"] * r**4        # if only E differed
    implied_rho = properties["rho"] / r**4    # if only rho differed
    implied_t = properties["t"] * r**2        # if only t differed

    print(material_name)
    print(f"  average ratio (hand / calculated): {r:.4f}")
    print(f"  if only E differed:   E   = {implied_E / 1e9:.1f} GPa     (I used {properties['E'] / 1e9:.1f} GPa)")
    print(f"  if only rho differed: rho = {implied_rho:.0f} kg/m3   (I used {properties['rho']} kg/m3)")
    print(f"  if only t differed:   t   = {implied_t * 1000:.3f} mm    (I used {properties['t'] * 1000:.3f} mm)")
