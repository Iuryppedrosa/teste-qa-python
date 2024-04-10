# Teste para Estagiário de QA

## Parte 1: Conhecimento Teórico

1. **Garantia de Qualidade (QA)**
   - **Pergunta:** Explique o que você entende por Garantia de Qualidade (QA) e qual a sua importância no desenvolvimento de software.

2. **Testes de Caixa Branca e Caixa Preta**
   - **Pergunta:** Diferencie testes de caixa branca e testes de caixa preta.

3. **Testes de Regressão**
   - **Pergunta:** O que são testes de regressão? Por que são importantes?

4. **Automação de Testes em Aplicações Streamlit**
   - **Pergunta:** Como você abordaria a automação de testes para uma aplicação Streamlit? Quais ferramentas você usaria?

5. **Importância da Documentação em QA**
   - **Pergunta:** Por que a documentação é importante no processo de Garantia de Qualidade (QA)? Como a documentação de testes contribui para o sucesso de um projeto de software?

## Parte 2: Habilidades Práticas

1. **Revisão de Código**
   **QA 1**
   - **Instrução:** Abaixo está um trecho de código Python usado em uma aplicação Streamlit. Identifique qualquer erro ou problema potencial que possa afetar a qualidade ou desempenho da aplicação.
     ```python
     import streamlit as st
     
     def calculate_interest(principal, rate, time):
         # Suponha que esta função tenha uma lógica complexa
         return (principal * rate * time) / 100
     
     principal = st.number_input("Principal Amount", value=1000)
     rate = st.number_input("Interest Rate", value=5)
     time = st.number_input("Time (in years)", value=1)
     interest = calculate_interest(principal, rate, time)
     st.write(f"The interest is {interest}")
     ```

2. **Cenário de Teste**
   - **Instrução:** Escreva um cenário de teste detalhado para a funcionalidade de cálculo de juros demonstrada no trecho de código acima. Inclua os passos para a execução do teste, os dados de entrada necessários e os resultados esperados.

3. **Automação de Teste**
   - **Instrução:** Com base no cenário de teste que você escreveu na questão anterior, crie um script de automação de teste usando uma ferramenta de sua escolha, adequado para uma aplicação Streamlit.

4. **Criação de Documentação de Teste**
   - **Instrução:** Considerando o cenário de teste que você elaborou para a funcionalidade de cálculo de juros em uma aplicação Streamlit, crie um exemplo de documentação de teste. Essa documentação deve incluir:
     - Uma descrição do objetivo do teste.
     - Pré-requisitos ou configurações necessárias antes de executar o teste.
     - Passos detalhados para a execução do teste.
     - Dados de entrada para o teste.
     - Resultados esperados.
     - Critérios para passar/falhar no teste.

## Parte 3: Resolução de Problemas

1. **Investigação de Bug**
   - **Instrução:** Imagine que um usuário relata um bug em uma aplicação Streamlit, onde o cálculo de juros não está considerando corretamente o valor do tempo (anos) inserido. Descreva os passos que você seguiria para reproduzir, investigar e sugerir uma correção para o problema.

2. **Análise de Documentação de Teste Existente**
   - **Pergunta:** Imagine que você recebeu uma documentação de teste de uma aplicação Streamlit para revisão. Quais aspectos você avaliaria para garantir que a documentação é clara, completa e útil para os testadores? Descreva como você abordaria a melhoria dessa documentação.

![](https://private-user-images.githubusercontent.com/89420889/321228084-4090582a-a5bc-4050-ab33-d8733b6279a9.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTI3NTA0MjUsIm5iZiI6MTcxMjc1MDEyNSwicGF0aCI6Ii84OTQyMDg4OS8zMjEyMjgwODQtNDA5MDU4MmEtYTViYy00MDUwLWFiMzMtZDg3MzNiNjI3OWE5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA0MTAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNDEwVDExNTUyNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWY1MTRlNmJhZTA2MzgzODk0NmE0MDE4ODYyM2I0ZTE0YWFmM2RlMzM4MTg5MTk0ZjFlNDk2MGI3OTlkZjBhZTQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.rF4jvsuteyoQlhCi9-DExGMXEMN9W9K97I7j1TadATw)
