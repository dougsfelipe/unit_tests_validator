import pytest
from validator import validar_cpf, validar_cep, validar_cnpj



def test_validar_cpf_valido():
    assert validar_cpf("529.982.247-25") == True
    assert validar_cpf("52998224725") == True
    assert validar_cpf("123.456.789-09") == True

def test_validar_cpf_invalido():
    assert validar_cpf("11111111111") == False
    assert validar_cpf("12345678900") == False
    assert validar_cpf("529.982.247") == False
    assert validar_cpf("abcdefghijk") == False
    assert validar_cpf("000.000.000-00") == False
    assert validar_cpf("") == False

def test_validar_cep_valido():
    assert validar_cep("12345-678") == True
    assert validar_cep("12345678") == True


def test_entrada_valida_cep():
    assert validar_cep("1234-567") == False
    assert validar_cep("12.345-678") == False


@pytest.mark.parametrize("cnpj_valido", [
    "04.252.011/0001-10",
    "04252011000110",
    "11.222.333/0001-81"  # válido fictício
])

def test_validar_cnpj_valido(cnpj_valido):
    assert validar_cnpj(cnpj_valido) == True

@pytest.mark.parametrize("cnpj_invalido", [
    "00.000.000/0000-00",   # repetido
    "11111111111111",       # repetido
    "12345678000100",       # dígitos errados
    "04.252.011/0001",      # incompleto
    "abcdefghijklll",       # letras
    "",                     # vazio
])

def test_validar_cnpj_invalido(cnpj_invalido):
    assert validar_cnpj(cnpj_invalido) == False

