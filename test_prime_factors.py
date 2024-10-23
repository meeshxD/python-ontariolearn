import pytest
from prime import generate_prime_factors
def test_1_string():
    with pytest.raises(ValueError, match = "Wrong data type, must be an integer"):
        generate_prime_factors("string")
def test_1_float():
    with pytest.raises(ValueError, match = "Wrong data type, must be an integer"):
        generate_prime_factors(1.0)
def test_2():
    assert generate_prime_factors(1) == []
def test_3():
    assert generate_prime_factors(2) == [2]
def test_4():
    assert generate_prime_factors(3) == [3]
def test_5():
    assert generate_prime_factors(4) == [2,2]
def test_6():
    assert generate_prime_factors(6) == [2,3]
def test_7():
    assert generate_prime_factors(8) == [2,2,2]
def test_8():
    assert generate_prime_factors(9) == [3,3]