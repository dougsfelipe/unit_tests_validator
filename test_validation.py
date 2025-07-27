import pytest

def test_validar_cpf_valido(cpf):
    assert validar_cpf(cpf) == True

def test_validar_cpf_invalido(cpf):
    assert validar_cpf(cpf) == False

def test_entrada_valida_cpf(cpf):
    assert validar_cpf(cpf) == "Entrada Invalida de CPF"


def test_validar_cep_valido(cep):
    assert validar_cep(cep) == True


def test_validar_ccep_invalido(cep):
    assert validar_cep(cep) == False


def test_entrada_valida_cep(cep):
    assert validar_cep(cep) == "Entrada Invalida de CEP"


def test_validar_cnpj_valido(cnpj):
    assert validar_cnpj(cnpj) == True


def test_validar_cnpj_invalido(cnpj):
    assert validar_cnpj(cnpj) == False


def test_entrada_valida_cnpj(cnpj):
    assert validar_cnpj(cnpj) == "Entrada Invalida de CNPJ"

