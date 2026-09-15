#Лабораторна робота №1. Основи Python
# Варіант: 1
# ПІБ: Армашева Олександра Іванівна

while True:
    try:
        length = float(input("Введіть довжину прямокутника: "))
        width = float(input("Введіть ширину прямокутника: "))

        if length <= 0 or width <= 0:
            raise ValueError("Числа повинні бути додатними")
        break
    except ValueError:
        print("Помилка! Введіть правильні числа.")

area = length * width
perimeter = 2 * (length + width)

print("\nРезультати:")
print(f"Площа прямокутника: {area:.2f} см²")
print(f"Периметр прямокутника: {perimeter:.2f} см")


if length == width:
    print("Це квадрат!")
    print("Довжина та ширина однакові")
elif length > width:
    print("Це витягнутий прямокутник.")
    print(f"Довжина більша на {length - width:.2f} см.")
else:
    print("Це широкий прямокутник.")
    print(f"Ширина більша на {width - length:.2f} см.")

answer = input("Хочете виконати ще одне обчислення? (так/ні): ")

if answer.lower() == "так":
     print("Запустіть програму ще раз.")
else:
  print("Дякую за використання програми!")
