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
hours = (minn // 60) % 24
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

## Лабораторная работа 2

### Задание номер 1
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    
    if len(nums) <= 0:
        raise ValueError
    return (min(nums),max(nums))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    
    nums = set(nums)
    nums = list(nums)
    return nums


def flatten(mat: list[list | tuple]) -> list:
    
    true_mat = []
    for i in mat:
        if not isinstance(i, (list, tuple)):
            raise TypeError
        for k in i:
            if isinstance(k,str):
                raise   TypeError
            
    for i in range(len(mat)):
        for k in mat[i]:
            true_mat.append(k)
    return true_mat
```
![Картинка 1](./images/lab02/01.png)
![Картинка 2](./images/lab02/02.png)
![Картинка 3](./images/lab02/03.png)

### Задание номер 2

```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    result = []

    if len(mat) == 1 and not mat[0]:
        return []
        
    for i in range(len(mat) - 1):
        if len(mat[i]) < len(mat[i+1]) or (len(mat[i]) > len(mat[i+1])):
            raise ValueError
    
    for i in range(len(mat[0])):
        new_list = []
        for k in range(len(mat)):
            new_list.append(mat[k][i])
        result.append(new_list)
    
    return result

def row_sums(mat: list[list[float | int]]) -> list[float]:
    
    sum_list = []
    
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            raise ValueError
        
    for i in range(len(mat)):
        summ = 0
        for k in mat[i]:
            summ += k
        sum_list.append(summ)
    return sum_list

def col_sums(mat: list[list[float | int]]) -> list[float]:

    sum_list = []

    if not mat or not mat[0]:
        return []

    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            raise ValueError
         
    for i in range (row_len):
        summ = 0
        for k in range(len(mat)):
            summ += mat[k][i]
        sum_list.append(summ)
    
    return sum_list
```

![Картинка 4](./images/lab02/04.png)
![Картинка 5](./images/lab02/05.png)
![Картинка 6](./images/lab02/06.png)

### Задание номер 3

```python
def format_record(rec: tuple[str, str, float]) -> str:
    fio_clean = rec[0].strip()
    FIO = fio_clean.split()

    gpa = round(rec[2], 2)

    if len(FIO) == 3:
        return f"{FIO[0][0].upper()}{FIO[0][1:]} {FIO[1][0].upper()}.{FIO[2][0].upper()}. , гр. {rec[1]}, GPA {gpa:.2f}"
    elif len(FIO) == 2:
        return f"{FIO[0]}{FIO[0][1:]} {FIO[1][0].upper()}. , гр. {rec[1]}, GPA {gpa:.2f}"
    else:
        raise ValueError
    
```
![Картинка 7](./images/lab02/07.png)

## Лабораторная работа 3

### Задание номер 1

```python
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    
    if casefold:
        text = text.casefold()
    
    if yo2e:
        text = text.replace('ё','е').replace("Ё","Е")
    
    for ch in ['\n', '\r', '\t']:
        text = text.replace(ch, ' ')
    
    while '  ' in text:
        text = text.replace('  ', ' ')

    return text.strip()

"""
legal_chars = set()

for i in range(65, 123):
    legal_chars.add(chr(i))


for i in range(1040, 1104):
    legal_chars.add(chr(i))

for i in range(0, 10):
    legal_chars.add(str(i)) 

legal_chars.update(['-', '_'])

def tokenize(text: str) -> list[str]:
    
    true_text = ''

    for ch in text:
        
        if ch in legal_chars:
            true_text += ch
        
        else:
            true_text += ' ' 
    
    true_text = normalize(true_text)
    
    return true_text.split()
"""

def tokenize(text: str) -> list[str]:

    text = normalize(text, casefold=True, yo2e=True)
    pattern = r'\w+(?:-\w+)*'

    return re.findall(pattern, text)

def count_freq(tokens: list[str]) -> dict[str, int]:

    sbor = {}

    for i in range (len(tokens)):

        if tokens[i] in sbor:
            continue

        else:
            sbor[tokens[i]] = tokens.count(tokens[i])

    return sbor

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    sorted_items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    
    return sorted_items[:n]

```

```python
from src.lib.text import *

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка", yo2e=True))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))


print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

print(top_n(count_freq(["a", "b", "a", "c", "b", "a"]), n=2))
print(top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), n=2))
```

![Картинка 1](./images/lab03/A.png)

### Задание номер 2

```python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.lib.text import*

text = sys.stdin.read()

textn = text

text = normalize(text)
text = tokenize(text)
textn = text
top = top_n(count_freq(text), n = 5)
text = top_n(count_freq(text))


print(f"Всего слов: {len(textn)}")
print(f"Уникальных слов: {len(text)}")
print("Топ-5:")
for word, count in top:
    print(f"{word}: {count}")
```

![Картинка 2](./images/lab03/B.png)