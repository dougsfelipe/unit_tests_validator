import re


def calcular_digito_cpf(cpf_parcial, peso):
    soma = sum(int(digito) * (peso - i) for i, digito in enumerate(cpf_parcial))
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)

def validar_cpf(cpf: str):
    cpf = re.sub(r'\D', '', cpf) #expressao regular para deixar somente os numeros

    digitoV1 = calcular_digito_cpf(cpf[:9], 10)
    digitoV2 = calcular_digito_cpf(cpf[:10], 11)

    if len(cpf) != 11 or cpf == cpf[0]*11:
        return False

    return cpf[-2:] == digitoV1 + digitoV2


def validar_cep(cep: str) -> bool:
    return bool(re.fullmatch(r"\d{5}-?\d{3}", cep))

def calcular_digito_cnpj(cnpj_parcial, pesos):
    soma = sum(int(d) * p for d, p in zip(cnpj_parcial, pesos))
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)

def validar_cnpj(cnpj: str) -> bool:
    cnpj = re.sub(r'\D', '', cnpj)

    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6] + pesos1

    digito1 = calcular_digito_cnpj(cnpj[:12], pesos1)
    digito2 = calcular_digito_cnpj(cnpj[:12] + digito1, pesos2)

    return cnpj[-2:] == digito1 + digito2


if __name__ == '__main__':
    test = input("digite CPD")
    print(validar_cep(test))