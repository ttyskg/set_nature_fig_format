# set_nature_fig_format

Script to set parameters to create figures according to [Nature's guidelines](https://www.nature.com/documents/nature-final-artwork.pdf).

## Supported environments

- debian-based WSL2

## Nature's guideline

- Standard figure sizing (width).
  - 89 mm (single column).
  - 120 mm.
  - 183 mm (double column).
- Standard figure sizing (depth).
  - Up to 170 mm.
- Fonts and text.
  - Font: sans-serif typeface (Helvetica or Arial)
  - Font for one-letter amino acid code: Courier
  - Font size: 5 pt - 7 pt
- Resolution:
  - Minimum: 300 dpi.
  - Maximum: 450 dpi (online proof).

## Usage

The `set_rcparams()` should be called before making figures.

```python
from set_nature_fig_format import set_rcparams

set_rcparams()

# then, make plots
fig, axs = fig.subplots()
...
```
