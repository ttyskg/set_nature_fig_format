"""test for set_parameters.py"""

import os

import matplotlib as mpl
import matplotlib.font_manager as fm

from set_parameters import add_font_family, set_rcparams


def test_set_rcparams():
    set_rcparams()
    mpl.rcParams["font.size"] == 5
    mpl.rcParams["xtick.major.size"] == 2


def test_add_font_family():
    # get font file directory path
    directory = os.path.dirname(__file__)
    fontpath = f"{directory}/fonts"

    # test Open Sans adding
    "Open Sans" not in fm.get_font_names()
    add_font_family(fontpath)
    "Open Sans" in fm.get_font_names()
