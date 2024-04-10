import pytest

import funcionalidade_agromercantil

def test_juros():
    principal = 1000
    rate = 5
    time = 1
    expected = 50

    juros_calculados = funcionalidade_agromercantil.calculate_interest(principal, rate, time)
    assert juros_calculados == expected, "Deu errado o calculo"


#Cenário de teste de Taxa de Juros com casas decimais.

"""Cenário pensado para garantir que o algoritimo saiba calcular
    o juros corretamente com casas decimais, visto que 
    é uma pratica recorrente no calculo de júros."""

def test_casas_decimais():
    principal = 1000
    rate = 5.5 #entrada com casas decimais
    time = 1.6

    # O valor esperado
    resultado_esperado = 88

    # Chama a função com os valores de ponto flutuante
    juros_calculados = funcionalidade_agromercantil.calculate_interest(principal, rate, time)

    assert juros_calculados == resultado_esperado
"""
Teste de casas decimais executando corretamente
"""
