import pytest
from validator import Validator

@pytest.fixture
def validar():
    return Validator()

@pytest.mark.parametrize("cpf_valido", [
    "529.982.247-25",
    "52998224725",
    "123.456.789-09"
])

def test_validar_cpf_valido(validar,cpf_valido):
    assert validar.validar_cpf(cpf_valido) == True

@pytest.mark.parametrize("cpf_invalido", [
    "11111111111",
    "12345678900",
    "000.000.000-00",
    "529.982.247",
    "abcdefghijk",

])

def test_validar_cpf_invalido(validar, cpf_invalido):
    assert validar.validar_cpf(cpf_invalido) == False

@pytest.mark.parametrize("cpf_formato_invalido", [
    52998224725,
    52998224725,
    12345678909
])

def test_validar_cpf_formato_invalido(validar, cpf_formato_invalido):
    with pytest.raises(ValueError):
        validar.validar_cpf(cpf_formato_invalido)


@pytest.mark.parametrize("cep_valido", [
    "12345-678",
    "12345678"
])

def test_validar_cep_valido(validar,cep_valido):
    assert validar.validar_cep(cep_valido) == True

@pytest.mark.parametrize("cep_invalido", [
    "1234-567",
    "12.345-678"
])

def test_validar_cep_invalido(cep_invalido, validar):
    assert validar.validar_cep(cep_invalido) == False

@pytest.mark.parametrize("cep_formato_invalido", [
    12345678,
    12345678
])

def test_validar_cep_formato_invalido(validar, cep_formato_invalido):
    with pytest.raises(ValueError):
        validar.validar_cpf(cep_formato_invalido)



@pytest.mark.parametrize("cnpj_valido", [
    "04.252.011/0001-10",
    "04252011000110",
    "11.222.333/0001-81"  # válido fictício
])

def test_validar_cnpj_valido(cnpj_valido,validar):
    assert validar.validar_cnpj(cnpj_valido) == True

@pytest.mark.parametrize("cnpj_invalido", [
    "00.000.000/0000-00",   # repetido
    "11111111111111",       # repetido
    "12345678000100",       # dígitos errados
    "04.252.011/0001",      # incompleto
    "abcdefghijklll",       # letras
    "",                     # vazio
])

def test_validar_cnpj_invalido(cnpj_invalido,validar):
    assert validar.validar_cnpj(cnpj_invalido) == False

@pytest.mark.parametrize("cnpj_formato_invalido", [
    11111111111111,
    12345678000100,
    14252011000110
])

def test_validar_cnpj_formato_invalido(validar, cnpj_formato_invalido):
    with pytest.raises(ValueError):
        validar.validar_cnpj(cnpj_formato_invalido)

