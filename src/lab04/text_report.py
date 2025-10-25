from src.lab04.io_txt_csv import *
from src.lib.text import *

#Задание А
a = read_text("C:\\VSprojects\\python_labs\\data\\lab04\\input.txt")
a = normalize(a)
a = tokenize(a)
a = count_freq(a)
a = top_n(a)

write_csv(
    rows = a, 
    path = "C:\\VSprojects\\python_labs\\data\\lab04\\report.csv",
    header=["Word","Count"]  
)

#Задание B

b = read_text("C:\\VSprojects\\python_labs\\data\\lab04\\input.txt")
b = normalize(b)
b = tokenize(b)
b_ = b
b = count_freq(b)
top = top_n(b,5)
b = top_n(b)


write_csv(
    rows = b, 
    path = "C:\\VSprojects\\python_labs\\data\\lab04\\report.csv",
    header=["Word","Count"]
)

print(f"Всего слов: {len(b_)}")
print(f"Уникальных слов: {len(b)}")
print("Топ-5:")
for word, count in top:
    print(f"{word}: {count}")