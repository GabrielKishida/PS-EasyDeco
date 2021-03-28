####################################################
# Processo Seletivo EasyDeco
# Algoritmo( para a validação de senhas
# Desenvolvido por: Gabriel Yugo Nascimento Kishida
# Contato : gabriel.kishida@usp.br
# Março de 2021
####################################################

import re

def valid_string_size(password) :
    valid = len(password) <=14 and len(password) >= 8
    if not valid :
        print("A sua senha tem tamanho inválido (deve conter de 8 a 14 caracteres).")
    return valid

def has_upper(password) :
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in upper :
        if char in password :
            return True
    print("A sua senha deve conter pelo menos um caractere maiúsculo.")
    return False
    
def has_lower(password) :
    upper = "abcdefghijklmnopqrstuvwxyz"
    for char in upper :
        if char in password :
            return True
    print("A sua senha deve conter pelo menos um caractere minúsculo.")
    return False

def has_number(password) :
    for char in password :
        if char.isdigit(): 
            return True
    print("A sua senha deve conter pelo menos um número.")
    return False

def has_specialchar(password) :
    specialchar = "/\[@_!#$%^&*()<>?}{~:]|"
    for char in specialchar :
        if char in password :
            return True
    print("A sua senha deve conter pelo menos um caractere especial.")
    return False

def repeats_sequence(password) :
    n = len(password)
    for i in range(n-2) :
        segpassword = password[i:i+2]
        if (password.count(segpassword) > 1) :
            print("A sua senha não pode conter uma sequência de caracteres repetidos.")
            return True
    return False

def multiple_validation(validations) :
    valid = True
    for validation in validations :
        valid = valid and validation
    return valid


def password_validation(password) :
    validations = []
    validations.append(valid_string_size(password))
    validations.append(has_upper(password))
    validations.append(has_lower(password))
    validations.append(has_number(password))
    validations.append(has_specialchar(password))
    validations.append(not repeats_sequence(password))
    valid = multiple_validation(validations)
    if valid :
        print("Senha válida.")
    return valid

password = input("Por favor insira a sua senha: ")
password_validation(password)