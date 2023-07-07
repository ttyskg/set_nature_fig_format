"""functions for setting matplotlib rc parameters."""


import matplotlib as mpl
from matplotlib import font_manager


# set matplotlib default parameters
def set_rcparams():
    """set matplotlib rc parameters

    Returns:
        No return, just modify mpl.rcParameters
    """
    # set font: sans-serif typeface is required,
    # preferable, Helvetica or Arial.
    available_fonts = font_manager.get_font_names()
    if "Helvetica" in available_fonts:
        mpl.rcParams["font.family"] = "Helvetica"
    elif "Helvetica LT Pro" in available_fonts:
        mpl.rcParams["font.family"] = "Helvetica LT Pro"
    elif "Arial" in available_fonts:
        mpl.rcParams["font.family"] = "Arial"
    else:
        raise ValueError("There is no Helvetica or Arial in the available font list.")

    # text size should be between 5 pt to 7 pt
    mpl.rcParams["font.size"] = 5
    mpl.rcParams["axes.titlesize"] = 6
    mpl.rcParams["xtick.labelsize"] = 5
    mpl.rcParams["ytick.labelsize"] = 5
    mpl.rcParams["legend.fontsize"] = 5

    # Optional settings: there is requirement in Nature's guideline
    mpl.rcParams["xtick.major.size"] = 2
    mpl.rcParams["xtick.minor.size"] = 1.2
    mpl.rcParams["ytick.major.size"] = 2
    mpl.rcParams["ytick.minor.size"] = 1.2
    mpl.rcParams["lines.linewidth"] = 1.2
    mpl.rcParams["lines.markersize"] = 2
    mpl.rcParams["lines.markeredgewidth"] = 0.5
    mpl.rcParams["boxplot.flierprops.markersize"] = 2
    mpl.rcParams["boxplot.flierprops.markeredgewidth"] = 0.5
    return 0


def add_font_family(path: str):
    """make specified font available to the FontManager.

    Args:
        path (str): directory path of font files
    """
    for font in font_manager.findSystemFonts(fontpaths=path):
        font_manager.fontManager.addfont(font)
    return 0
