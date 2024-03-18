# 2)
def fibonacci(n):
    fib_sequence = [0, 1]  # Inicializa a sequência de Fibonacci com os dois primeiros números
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Adiciona o próximo número à sequência
    return fib_sequence

def verifica_fibonacci(numero):
    fib_sequence = fibonacci(numero)  # Calcula a sequência de Fibonacci até o número informado
    if numero in fib_sequence:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

# Exemplo de uso
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
print(verifica_fibonacci(numero))