def inverter_string(string):
    inverted_string = ""
    for char in string:
        inverted_string = char + inverted_string
    return inverted_string

# Exemplo de uso
entrada = input("Digite uma string para inverter: ")
resultado = inverter_string(entrada)
print("String original:", entrada)
print("String invertida:", resultado)
