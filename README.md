# Music box tine calculator

A Python tool that recalculates the tine lengths of a music box comb and checks them against the hand calculations in our group design report. It found that the report's stated material properties do not reproduce its own table of lengths.

## Background

As part of a group design project at Imperial College London, we made an automated, app-controlled music box with interchangeable combs of different materials, which could be analysed for materials characterisation. The three combs were 1 mm brass, 1 mm spring steel and 3 mm PMMA.

My role included calculating the comb dimensions: the length each tine needs to be to play a given note. The report uses this equation (Equation 1):

f = (0.162 × t / L²) × √(E/ρ)

where f is frequency, t is tine thickness, L is tine length, E is Young's modulus and ρ is density. Rearranged for length:

L = √(0.162 × t × √(E/ρ) / f)

The report lists hand-calculated lengths for 16 notes in each of the 3 materials (48 lengths).

## What I built

- **`tine_calculator.py`** recalculates all 48 lengths from the equation and the material properties stated in the report, compares each with the hand-calculated value as a percentage difference, and saves the results to `tine_lengths_results.csv`.
- **`investigate.py`** works backwards from the hand-calculated lengths to find which values of E, ρ or t would explain the differences.
- **`DECISIONS.md`** is a log of the choices made along the way and why.

## What I found

Every calculated length differed from the hand-calculated value, and each material had its own steady offset:

| Material | Average difference | Range across 16 notes |
|---|---|---|
| Brass (1 mm) | +1.18% | +1.04% to +1.29% |
| Spring steel (1 mm) | −2.47% | −2.61% to −2.37% |
| PMMA (3 mm) | −3.57% | −3.64% to −3.45% |

How I narrowed down the cause:

- **Not rounding.** The hand values are given to 0.01 cm, which can only explain differences of up to about 0.2%. These are 5 to 15 times bigger.
- **Not frequency.** The offset barely changes from the lowest note (196 Hz) to the highest (1046.5 Hz), so the cause does not depend on frequency.
- **Not the equation.** An error in the equation, such as a wrong constant, would shift all three materials by the same amount. Instead each material has a different offset, so the cause belongs to each material: its E, ρ or t.

I then checked the report itself. Its equation is the same as the one in my code, and the E and ρ values it states are the ones I used. So the report's table cannot be reproduced from the report's own stated inputs: the hand calculations must have used different material values from those written down. The report also never states a density for spring steel.

`investigate.py` shows what the inputs would have needed to be. Since length depends on (E/ρ)^¼, a 1% difference in length needs about a 4% difference in E/ρ.

The calculator keeps the report's stated values rather than adjusting them to match the table, so the inconsistency stays visible rather than hidden.

## Decisions and trade-offs

Full reasoning is in [`DECISIONS.md`](DECISIONS.md). In short:

- **Python's built-in `csv` module rather than pandas.** The input is a 16-row table, so `csv` is enough, needs nothing installed and keeps every line explainable.
- **Lengths reported to 2 decimal places (0.01 cm).** This matches the report and the precision of the laser cutter; percentage differences are worked out from unrounded values.
- **Keep the stated material values and report the discrepancy** rather than tuning the values until the numbers agree.

## What I learnt

- Writing and testing a Python function from an engineering equation, and keeping all calculations in SI units.
- Reading and writing CSV files with Python's `csv` module.
- Using Git to track a project in small, clearly described commits.
- Checking results systematically: using the pattern of the errors (steady per material, independent of frequency) to rule out causes one at a time.
- Recording inputs properly. The report quoted one set of property values, the calculations used another, and nobody recorded which. Next time I would write down the source of every input next to the calculation, so anyone checking the work can reproduce it.

## How to run it

You need Python 3. Nothing else needs installing.

```
python tine_calculator.py
python investigate.py
```

The first command writes `tine_lengths_results.csv`. The second prints the back-calculated material properties.

## Files

| File | What it is |
|---|---|
| `tine_calculator.py` | Material properties, the `tine_length` function, and the main calculation |
| `investigate.py` | Back-calculates the inputs the hand calculations must have used |
| `tine_lengths_report_table.csv` | Notes, frequencies and hand-calculated lengths from the report |
| `tine_lengths_results.csv` | Output: calculated lengths and percentage differences for all 48 tines |
| `DECISIONS.md` | Log of decisions and reasoning |
