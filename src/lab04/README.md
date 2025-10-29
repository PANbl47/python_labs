## Лабораторная работа 4

```python
from src.lab04.io_txt_csv import *
from src.lib.text import *

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
```

```python
import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encording: str = "cp1251") -> str:

    p = Path(path)

    if p.exists() == False:
        raise FileNotFoundError
    
    if len(p.read_text(encoding = encording)) <= 0:

        return '' 
    
    return p.read_text(encoding = encording)

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:

    p = Path(path)
    rows = list(rows)

    for i in range (len(rows)-1):

        if len(rows[i]) != len(rows[i+1]):
            raise ValueError

    with p.open("w", newline="", encoding="cp1251") as f:
        w = csv.writer(f)

        if header is not None:
            w.writerow(header)

        for r in rows:
            w.writerow(r)
```

### Задание номер А
![Картинка 1](./images/lab04/41.png)
![Картинка 2](./images/lab04/42.png)
![Картинка 3](./images/lab04/43.png)

### Задание номер B
![Картинка 1](./images/lab04/44.png)
![Картинка 2](./images/lab04/45.png)
![Картинка 3](./images/lab04/46.png)

### Задание номер С
![Картинка 1](./images/lab04/47.png)
![Картинка 2](./images/lab04/48.png)
![Картинка 3](./images/lab04/49.png)