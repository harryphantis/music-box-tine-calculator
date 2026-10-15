# Decisions log

Each entry records a real choice: what was chosen, the alternatives, and why.

## 15 Oct 2026: csv module instead of pandas

Python's built-in csv module, not pandas. The input is a 16-row table, so csv handles it easily, needs nothing installed, and keeps every line simple enough for me to explain. Pandas is the standard tool for larger datasets and I plan to learn it alongside SQL, but adding it tonight would have meant code I couldn't fully explain yet.
