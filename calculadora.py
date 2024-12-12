# calculadora.py

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) - 32 #erro na zoas

