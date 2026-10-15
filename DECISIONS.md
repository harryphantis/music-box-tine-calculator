# Decisions log

Each entry records a real choice: what was chosen, the alternatives, and why.

## 15 Oct 2026: csv module instead of pandas

Python's built-in csv module, not pandas. The input is a 16-row table, so csv handles it easily, needs nothing installed, and keeps every line simple enough for me to explain. Pandas is the standard tool for larger datasets and I plan to learn it alongside SQL, but adding it tonight would have meant code I couldn't fully explain yet.

## 15 Oct 2026: Lengths reported to 2 decimal places (0.01 cm)

Chose: round calculated lengths to 2 dp in the output, matching the hand-calculated table in the report. Percentage differences are calculated from the unrounded values.

Alternatives: full precision everywhere, or rounding before comparing.

Why: 2 dp makes the results directly comparable with the report's table. 0.01 cm is 0.1 mm, finer than the laser cutter could actually make (we widened the comb gap from 0.3 to 0.6 mm because it couldn't hold the tolerance), so more digits would be false precision. Comparing unrounded values stops rounding error from showing up as a fake discrepancy.

## 15 Oct 2026: Keep the report's stated material values; report the discrepancy rather than hide it

Chose: the calculator uses the E and ρ values stated in the report, not values adjusted to reproduce the report's table.

Alternatives: tune E and ρ until the calculated lengths match the hand-calculated table.

Why: the code reproduces the report's Equation 1 exactly, but every material shows a constant offset across all 16 notes (brass about +1.2%, spring steel about −2.5%, PMMA about −3.6%). A constant per-material offset rules out rounding (under about 0.2%) and the formula (which would shift all materials equally), so the hand calculations must have used different E and ρ values from those written in the report. The report also never states a density for spring steel. Tuning the values would make the numbers agree but hide the inconsistency. Lesson: record every input and its source alongside a calculation, so it can be reproduced.
