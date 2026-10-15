# Decisions log

Each entry records a real choice: what was chosen, the alternatives, and why.

## 15 Oct 2026: csv module instead of pandas

Python's built-in csv module, not pandas. The input is a 16-row table, so csv handles it easily, needs nothing installed, and keeps every line simple enough for me to explain. Pandas is the standard tool for larger datasets and I plan to learn it alongside SQL, but adding it tonight would have meant code I couldn't fully explain yet.

## 15 Oct 2026: Lengths reported to 2 decimal places (0.01 cm)

Chose: round calculated lengths to 2 dp in the output, matching the hand-calculated table in the report. Percentage differences are calculated from the unrounded values.

Alternatives: full precision everywhere, or rounding before comparing.

Why: 2 dp makes the results directly comparable with the report's table. 0.01 cm is 0.1 mm, finer than the laser cutter could actually make (we widened the comb gap from 0.3 to 0.6 mm because it couldn't hold the tolerance), so more digits would be false precision. Comparing unrounded values stops rounding error from showing up as a fake discrepancy.
