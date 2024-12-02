# -*- coding: utf-8 -*-

"""
aligned_semantic_distance
==========================

Code to implement the semantic distance between two transcriptions defined in https://doi.org/10.21437/Interspeech.2022-817

.. automodule:: aligned_semantic_distance.asd_metric
   :members:

"""

__author__ = """Janine Rugayan"""
__email__ = 'janine.rugayan@ntnu.no'
__version__ = '0.0.1'

from aligned_semantic_distance.asd_metric import (
    get_asd_output,
    print_alignment
)


VERSION = "0.0.1"

import sys

# Only print in interactive mode
# https://stackoverflow.com/questions/2356399/tell-if-python-is-in-interactive-mode/2356427#2356427
import __main__ as main
if bool(getattr(sys, 'ps1', sys.flags.interactive)):
    print("""Importing the aligned_semantic_distance module. When using in academic works please cite:
  Janine Rugayan and Torbjørn Svendsen and Giampiero Salvi (2022). Semantically Meaningful Metrics for Norwegian ASR Systems. In Interspeech, pp. 2283-2287, doi:10.21437/Interspeech.2022-817.\n""")
