# Processo Seletivo - EasyDeco
Neste repositório, existe o programa desenvolvido para atender ao teste de programação do processo seletivo da EasyDeco.

## O problema:
O problema a ser resolvido é o seguinte:

Validação de padrão de senha, utilizando os seguintes critérios:

1. Mínimo de 8 caracteres;
2. Máximo de 14 caracteres;
3. Obrigatório pelo menos um caracter maíusculo, um minúsculo, um número e um caracter especial;
4. Não é permitido repetir a mesma sequencia de caracteres;

## Resolução :
A resolução escolhida para o problema foi desenvolvida em Python, e pode ser visualizada [aqui](/passwordvalidation.py).

Para simplificar a resolução, decidiu-se segmentar o problema, criando funções que avaliam se a senha (recebida em formato String) é válida para os diferentes critérios. Então, por exemplo, criou-se uma função que avalia se a senha tem o tamanho válido (pelo menos 8 caracteres, e no máximo 14 caracteres).

Feitas essas funções auxiliares de avaliação de critérios, basta criar uma função principal (**password_validation**) que utiliza todas essas auxiliares. A senha só pode ser considerada válida se passar em todos os critérios. Se a senha não passar em pelo menos um deles, ela deve ser considerada inválida.

Nessa função principal, determinou-se que será retornado *True* caso a senha seja válida, e *False* caso contrário.

Além disso, mensagens deverão ser impressas explicitando se a senha passou por todos critérios ou não. Caso contrário, deve-se dizer qual o critério que não foi cumprido.
