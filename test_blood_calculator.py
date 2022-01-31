#test_blood_calculator.py

import pytest

from blood_calculator import check_HDL

@pytest.mark.parametrize("input_HDL, expected", [
    [70, "Normal"],
    [45, "Borderline Low"],
    [20, "Low"]
    ])
def test_check_HDL(input_HDL, expected):
    answer = check_HDL(input_HDL)
    assert answer == expected
    
##Look into pep 8 style guide
    
<<<<<<< HEAD
#pytest -v --pycodestyle

#pylint
=======
>>>>>>> 5873fe1fc004717bc5943a7d2f648345dde66981
