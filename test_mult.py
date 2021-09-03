import pytest
from multi import cal_mult, letra

#Calcular alguns números tanto positivo quanto negativo usando a multiplicação
@pytest.mark.parametrize('a,b,expected', [(4, 4, 16.0), (5 ,5 , 25.0), (-4 ,5 , -20)])
def test_calc(a,b, expected):
    assert cal_mult(a,b) == expected
#Calculando alguns números incluindo uma letra
@pytest.mark.parametrize('a,expected', [(78, 65, 5070), (70, 888, 62160.0), (12, 'a',False)])
def test_negativ(a,b,expected):
    assert letra(a,b) == expected
