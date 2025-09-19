# python_labs

## Лабораторная работа 1

### Задание номер 1
```python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
![Картинка 1](./images/lab01/01.png)

### Заданиет номер 2
```python
number01 = float(input("a: ").replace(",", "."))
number02 = float(input("b: ").replace(",", "."))
print(f"sum={number01 + number02}; avg={round(((number01 + number02) / 2),2)}")
```
![Картинка 2](./images/lab01/02.png)

### Задание номер 3
```python
price = 1000
discount = 10
vat = 20
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {format(base,'.2f')}")
print(f'НДС: {format(vat_amount,'.2f')}')
print(f"Итого к оплате: {format(total,".2f")}")
```
![Картинка 3](./images/lab01/03.png)

### Задание номер 4
```python
minn = int(input("Минуты: "))
hours = minn // 60
minn_time = (minn % 60)
if minn_time < 10:
    minn_time = "0" + str(minn_time)
print(f"{hours}:{minn_time}")
```
![Картинка 4](./images/lab01/04.png)

### Задание номер 5
```python
FIO = input("ФИО: ")
countt = 0
while '  ' in FIO:
    FIO = FIO.replace('  ', ' ')
words = FIO.split()
FIO_w_2spases = FIO.rstrip().lstrip()
first_letters = []
str_first_letters = ''
for word in words:
    first_letters.append(word[0])
for letter in first_letters:
    str_first_letters +=  letter
print(f"Инициалы: {str_first_letters}")
print(f"Длина (символов): {len(FIO_w_2spases)}")
```
![Картинка 5](./images/lab01/05.png)

## Задание номер 6
```python
n = int(input("Пришло людей: "))
ochno = zaochno = 0
for i in range(n):
    info = input().split()
    if info[3] == "True":
        ochno += 1
    else:
        zaochno += 1

print(f"Очно: {ochno}; Заочно: {zaochno}")
```
![Картинка 6](./images/lab01/06.png)
