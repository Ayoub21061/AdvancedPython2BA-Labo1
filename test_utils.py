import pytest
import utils
import numpy as np

def test_fact():
    assert utils.fact(4) == 24

def test_roots():
    m = [1, -3, 2]
    calculated_roots = utils.roots(m)
    assert list (calculated_roots) == [2, 1]


def test_integral():
    expected_value = 0  # Valeur attendue de l'intégrale
    calculated_value = utils.integral()  # Appel de la fonction pour calculer l'intégrale
    assert calculated_value == expected_value



