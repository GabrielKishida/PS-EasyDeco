####################################################
# Processo Seletivo EasyDeco
# Algoritmo( para a validação de senhas
# Desenvolvido por: Gabriel Yugo Nascimento Kishida
# Contato : gabriel.kishida@usp.br
# Março de 2021
####################################################

import re

def valid_string_size(password) :
    return len(password) <=14 and len(password) >= 8

def has_upper(password) :
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in upper :
        if char in password :
            return True
    return False
    
def has_lower(password) :
    upper = "abcdefghijklmnopqrstuvwxyz"
    for char in upper :
        if char in password :
            return True
    return False

def has_number(password) :
    has_number = False
    for char in password :
        if char.isdigit(): 
            has_number = True
            break
    return has_number

def has_specialchar(password) :
    specialchar = "/\[@_!#$%^&*()<>?}{~:]|"
    for char in specialchar :
        if char in password :
            return True
    return False

def repeats_sequence(password) :
    n = len(password)
    for i in range(n-2) :
        segpassword = password[i:i+2]
        if (password.count(segpassword) > 1) :
            return True
    return False

def password_validation(password) :
    valid = True
    if(not valid_string_size(password)) :
        print("A sua senha tem tamanho inválido (deve conter de 8 a 14 caracteres).")
        valid = False
    if(not has_upper(password)) :
        print("A sua senha deve conter pelo menos um caractere maiúsculo.")
        valid = False
    if(not has_lower(password)) :
        print("A sua senha deve conter pelo menos um caractere minúsculo.")
        valid = False
    if(not has_number(password)) :
        print("A sua senha deve conter pelo menos um número.")
        valid = False
    if(not has_specialchar(password)) :
        print("A sua senha deve conter pelo menos um caractere especial.")
        valid = False
    if(repeats_sequence(password)) :
        print("A sua senha não pode conter uma sequência de caracteres repetidos.")
        valid = False
    if(valid) :
        print("Senha válida.")
    return valid

password = input("Por favor insira a sua senha: ")
password_validation(password)