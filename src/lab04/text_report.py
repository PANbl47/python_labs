from src.lab04.io_txt_csv import *
from src.lib.text import *

p = read_text("C:\\VSprojects\\python_labs\\data\\lab04\\input.txt")
p = normalize(p)
p = tokenize(p)
p = count_freq(p)
p = top_n(p)

print(write_csv(
    rows = p, 
    path = "C:\\VSprojects\\python_labs\\data\\lab04\\report.csv",
    header=["Слово","Кол-во"]  
))

