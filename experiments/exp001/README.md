# exp001

## Purpose

Evaluate whether Wiktionary-based normalization improves embedding search quality.

---

## Hypothesis

Lemma normalization improves MRR.

---

## Dataset

- jawiki-20260401
- sample size: 100000

---

## Result

| metric | baseline | proposed |
|---|---:|---:|
| MRR | 0.612 | 0.644 |

---

## Observation

Normalization improved robustness against orthographic variations.

---

## Next Actions

Evaluate vocabulary filtering.