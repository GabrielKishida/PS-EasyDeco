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
    return not password.islower()
    
def has_lower(password) :
    return not password.isupper()

def has_number(password) :
    has_number = False
    for char in password :
        if char.isdigit(): 
            has_number = True
            break
    return has_number

def has_specialchar(password) :
    regex = re.compile("/\[@_!#$%^&*()<>?}{~:]|")
    if (regex.search(password) == None) :
        return False
    else :
        return True
    
def repeats_sequence(password) :
    n = len(password)
    for i in range(n-2) :
        segpassword = password[i:i+2]
        if (password.count(segpassword) > 1) :
            return True
    return False