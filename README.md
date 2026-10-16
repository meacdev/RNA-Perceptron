# RNA-Perceptron

## Sobre o repositório
Este repositório foi criado por Matheus Costa e Abner Tadeu para a conclusão de um projeto prático para a disciplina de Redes Neurais Artificiais ministrada no segundo semestre de 2026 na Universidade do Amazonas
### Resumo
A instrução para execução do projeto foi repassada pela professora Elloá Guedes, englobando três partes principais:
- Parte I - Resolvendo um problema linearmente separável
- Parte II - Experimentação
- Parte III - Validação Holdout em problema não-linearmente separável

A descrição de cada parte está disponível nas Issues do projeto.
### Objetivos
O objetivo da atividade foi exercitar nosso conhecimento na unidade introdutória à redes neurais, mais especificamente no modelo de neurônio chamado Perceptron, além de nossos conhecimentos em programação e linguagem python.

## Como rodar os notebooks?
Versão do Python: 3.15  
Justificativa: Utilizar a nova técnica de otimização de software chamada _lazy import_

Você precisará construir três datasets na seguinte estrutura:  
[valor1, valor2, classe0 ou classe1],  
[valor3, valor4, classe0 ou classe1],  
...  
E configurar os caminhos no arquivo .env  
Tenha ciência de que os dois primeiros datasets devem ser problemas linearmente separáveis e o último não deve ser.

As bibliotecas utilizadas estão em `requirements.txt`