####################################################
# Processo Seletivo EasyDeco
# Algoritmo para a validação de senhas
# Desenvolvido por: Gabriel Yugo Nascimento Kishida
# Contato : gabriel.kishida@usp.br
# Março de 2021
####################################################

### Definição de Funções Auxiliares ###

# Funcionalidade: valida se a senha tem tamanho válido
# Analisa o número de caracteres na String. 
# Se estiver no intervalo correto, retorna True. Caso contrário, retorna False.
def valid_string_size(password) :
    valid = len(password) <=14 and len(password) >= 8
    if not valid :
        print("A sua senha tem tamanho inválido (deve conter de 8 a 14 caracteres).")
    return valid

# Funcionalidade: valida se a senha tem pelo menos uma letra maiúscula.
# Percorre as letras maiúsculas até encontrar alguma que esteja na senha.
# Se encontrar alguma, retorna True. Caso contrário, retorna False.
def has_upper(password) :
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in upper :
        if char in password :
            return True
    print("A sua senha deve conter pelo menos um caractere maiúsculo.")
    return False

# Funcionalidade: valida se a senha tem pelo menos uma letra minúscula.
# Percorre as letras minúsculas até encontrar alguma que esteja na senha.
# Se encontrar alguma, retorna True. Caso contrário, retorna False.
def has_lower(password) :
    upper = "abcdefghijklmnopqrstuvwxyz"
    for char in upper :
        if char in password :
            return True
    print("A sua senha deve conter pelo menos um caractere minúsculo.")
    return False

# Funcionalidade: valida se a senha tem pelo menos um algarismo.
# Percorre a senha, até encontrar um dígito.
# Se encontrar algum, retorna True. Caso contrário, retorna False.
def has_number(password) :
    for char in password :
        if char.isdigit(): 
            return True
    print("A sua senha deve conter pelo menos um número.")
    return False

# Funcionalidade: valida se a senha tem pelo menos um caractere especial.
# Percorre os caracteres especiais, até encontrar um que esteja na senha.
# Se encontrar algum, retorna True. Caso contrário, retorna False.
def has_specialchar(password) :
    specialchar = "/\[@_!#$%^&*()<>?}{~:]|"
    for char in specialchar :
        if char in password :
            return True
    print("A sua senha deve conter pelo menos um caractere especial.")
    return False

# Funcionalidade: valida se a senha repete uma sequência de caracteres (não pode repetir)
# Percorre a senha, selecionando todos os pares sequenciais de caracteres menos o último (é possível que
# uma substring maior do que 2 se repita, mas só é necessário avaliar o menor caso).
# Se encontrar um par que se repete (aparece mais de uma vez), então retorna True. Se não, retorna False.
def repeats_sequence(password) :
    n = len(password)
    for i in range(n-2) :
        segpassword = password[i:i+2]
        if (password.count(segpassword) > 1) :
            print("A sua senha não pode conter uma sequência de caracteres repetidos.")
            return True
    return False

# Funcionalidade: verifica se todas as validações são True. 
# Retorna False se houver ao menos 1 False. Retorna True caso contrário.
def multiple_validation(validations) :
    valid = True
    for validation in validations :
        valid = valid and validation
        if (not valid) : return valid
    return valid

### Função principal ###
# Esta função é responsável por receber uma senha (password) em String, e
# avalia se a senha passa por todos os critérios requeridos. Caso passe,
# imprime que a senha é válida e retorna True. Caso contrário, imprime
# qual critério não foi validado e retorna False.
def password_validation(password) :
    validations = []
    validations.append(valid_string_size(password))
    validations.append(has_upper(password))
    validations.append(has_lower(password))
    validations.append(has_number(password))
    validations.append(has_specialchar(password))
    validations.append(not repeats_sequence(password))
    # Se um novo critério tiver que ser inserido, basta colocar validations.append(critério(password))
    valid = multiple_validation(validations)
    if valid :
        print("Senha válida.")
    return valid

### Main ###
# Esta seção constitui um exemplo no qual a função principal poderia ser chamada.
password = input("Por favor insira a sua senha: ")
password_validation(password)
