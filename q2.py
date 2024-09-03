def is_fibonacci(num):
    fib1, fib2 = 0, 1
    while fib1 <= num:
        if fib1 == num:
            return True
        fib1, fib2 = fib2, fib1 + fib2
    return False

numero = int(input("Digite um número: "))
if is_fibonacci(numero):
    print(f"O número {numero} está na sequência de Fibonacci.")
else:
    print(f"O número {numero} não está na sequência de Fibonacci.")
