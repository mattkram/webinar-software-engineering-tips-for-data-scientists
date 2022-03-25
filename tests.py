import pytest
from testbook import testbook


@testbook('analysis.ipynb', execute=True)
def test_celsius_to_fahrenheit(tb):
    celsius_to_fahrenheit = tb.ref("celsius_to_fahrenheit")
    assert celsius_to_fahrenheit(0.0) == 32.0
    