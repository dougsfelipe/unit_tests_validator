import re

class Validator:

    @staticmethod
    def validar_cpf(cpf: str):

        if not isinstance(cpf, str):
            raise ValueError("CPF deve ser uma string")

        cpf = re.sub(r'\D', '', cpf) #expressao regular para deixar somente os numeros

        def calcular_digito_cpf(cpf_parcial, peso):
            soma = sum(int(digito) * (peso - i) for i, digito in enumerate(cpf_parcial))
            resto = soma % 11
            return '0' if resto < 2 else str(11 - resto)

        digitoV1 = calcular_digito_cpf(cpf[:9], 10)
        digitoV2 = calcular_digito_cpf(cpf[:10], 11)

        if len(cpf) != 11:
            return  False

        if cpf == cpf[0] * 11:  # CPF com todos os dígitos iguais é inválido
            return False

        return cpf[-2:] == digitoV1 + digitoV2

    @staticmethod
    def validar_cep(cep: str) -> bool:
        if not isinstance(cep, str):
            raise ValueError("CEP deve ser uma string")

        cep_limpo = re.sub(r'\D', '', cep)

        if len(cep_limpo) != 8:
            return False

        # Regex aceita '12345678' ou '12345-678'
        return bool(re.fullmatch(r"\d{5}-?\d{3}", cep))

    @staticmethod
    def validar_cnpj(cnpj: str) -> bool:
        if not isinstance(cnpj, str):
            raise ValueError("CNPJ deve ser uma string")

        cnpj = re.sub(r'\D', '', cnpj)

        if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
            return False

        def calcular_digito_cnpj(cnpj_parcial, pesos):
            soma = sum(int(d) * p for d, p in zip(cnpj_parcial, pesos))
            resto = soma % 11
            return '0' if resto < 2 else str(11 - resto)

        pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos2 = [6] + pesos1

        digito1 = calcular_digito_cnpj(cnpj[:12], pesos1)
        digito2 = calcular_digito_cnpj(cnpj[:12] + digito1, pesos2)

        return cnpj[-2:] == digito1 + digito2

