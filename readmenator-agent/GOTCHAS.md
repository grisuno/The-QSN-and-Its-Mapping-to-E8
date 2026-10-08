# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `main.c` (score: 1.10)
- `life.py` (score: 0.70)
- `someideas.py` (score: 0.50)
- `someideas2.py` (score: 0.50)
- `transmision_qbits.py` (score: 0.30)
- `main.py` (score: 0.20)

## Hotspots (complexity + centrality)

- `life.py` -- complexity: 0.6, centrality: 1.0, combined: 0.9
- `someideas2.py` -- complexity: 0.5, centrality: 1.0, combined: 0.8
- `main.c` -- complexity: 1.0, centrality: 0.6, combined: 0.7
- `someideas.py` -- complexity: 0.5, centrality: 0.6, combined: 0.5
- `transmision_qbits.py` -- complexity: 0.3, centrality: 0.6, combined: 0.5
- `main.py` -- complexity: 0.2, centrality: 0.6, combined: 0.4

## Dataflow Issues (INFERRED, review each lead)

- `main.c:55` `generate_quasicrystal_tetrahedron` [DEAD_STORE] `y`: `y` assigned at line 55 but never read afterwards.
- `main.c:56` `generate_quasicrystal_tetrahedron` [DEAD_STORE] `z`: `z` assigned at line 56 but never read afterwards.
