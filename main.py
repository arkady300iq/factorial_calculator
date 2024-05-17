def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    try:
        num = int(input("Введіть число: "))
        result = factorial(num)
        print("Факторіал числа", num, "дорівнює", result)
    except ValueError:
        print("Будь ласка, введіть ціле число.")
main()
