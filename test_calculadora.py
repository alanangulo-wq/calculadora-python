from calculadora import Calculadora

def test_add():
    calc = Calculadora()
    assert calc.add(2, 3) == 5

def test_multiply():
    calc = Calculadora()
    assert calc.multiply(2, 3) == 6