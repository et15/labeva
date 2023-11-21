## v2.1.0rc0 (2023-11-21)

### Fix

- **project**: add missing dependency lmfit with version >=1.2.0

## v2.1.0a3.dev1 (2023-07-16)

### Fix

- **plot**: fix plot & errorbar argument functions regarding getting arguments from locals()

## v2.1.0a2.dev1 (2023-07-14)

### Fix

- **plot**: fix typo in function signature
- **labeva**: fix git versioning. files `fit.py` and `plot.py` where known twice (upper and lower case first letter)
- **project**: fix dependencies

### Refactor

- **project**: fixed imports for mkdocs and put them in a group
- **project**: requirements changed to: python = ">=3.10,<3.13"
- **labeva**: some small changes like changing the parameter sequence

## v2.1.0a1.dev1 (2023-07-13)

### Fix

- **labeva**: fixed imports

## v2.1.0a0.dev1 (2023-07-13)

### Feat

- **project**: Commitizen: sign tags

### Fix

- **project**: fix import of labeva in pyproject.toml

### Refactor

- **project**: change location of version file
- **func,-math**: renamed modules fo func and math

## v2.0.1 (2023-07-12)

### Feat

- **ALL**: create first reloaded version of labeva with lmfit
