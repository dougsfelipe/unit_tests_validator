# Projeto de Validação com Pytest

![CI](https://github.com/dougsfelipe/unit_tests_validator/actions/workflows/python-tests.yml/badge.svg)

Este projeto contém funções em Python com testes automatizados usando **Pytest** e integração contínua via **GitHub Actions**.

---

## 🚀 Funcionalidades

- Validação de CPF
- Validação de CEP
- Validação de CNPJ (em breve)
- Cálculos matemáticos (soma, subtração, divisão e multiplicação)
- Cálculo de desconto
- FizzBuzz com TDD

---

## 🧪 Testes

Os testes são escritos com [Pytest](https://docs.pytest.org/) e são executados automaticamente no GitHub Actions a cada `push` na branch `master`.

### ✅ Rodar os testes localmente:

![Print dos resultados](./unit_test_results.png)

```bash
pip install -r requirements.txt
pytest 

