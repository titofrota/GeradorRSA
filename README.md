# Gerador/Verificador de Assinaturas RSA

# Segurança Computacional - UnB - 2020/2
 - Ítalo Frota - 18/0019279 
 - João Melo - 16/0127670

O repositório contém o trabalho final da disciplina de Segurança Computacional ministrada na Universidade de Brasília no semestre 2020/2. 

O trabalho consiste na implementação de um Gerador/Verificador de Assinaturas RSA com as seguintes funcionalidades:
- Geração de chaves (mínimo de 1024 bits)
- Assinatura 
1. Cálculo de hashes (função de hash SHA-3) 
2. Assinatura da mensagem (cifração do hash)
3. Formatação do resultado (caracteres especiais e informações para verificação) 

- Verificação 
5. Parsing do documento assinado (de acordo com a formatação usada)
6. Decifração da assinatura (decifração do hash)
7. Verificação (cálculo e comparação do hash do arquivo)

# O que foi implementado?
 

 - [x] Geração de chaves
 - [x] Cifração
 - [x] Decifração
 - [x] Assinatura
 - [x] Verificação
 - [x] OAEP
 - [x] Formatação/parsing

