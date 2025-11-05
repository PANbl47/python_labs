## Лабораторная работа 5
### Задание номер 1

```python
import csv
import json
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный.
    """

    json_path = Path(json_path)

    if json_path.exists() == False:
        raise FileNotFoundError
    
    if len(json_path.read_text(encoding = "utf-8")) <= 0:
        raise ValueError

    with json_path.open("r",newline="",encoding = 'utf-8') as f:
        json_import = json.load(f)

    csv_path = Path(csv_path)

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        csv_writer = csv.DictWriter(f,fieldnames = ["name",'age','city'])

        csv_writer.writeheader() 
        csv_writer.writerows(json_import)      



def csv_to_json(csv_path: str, json_path: str) -> None:

    json_path = Path(json_path)
    csv_path = Path(csv_path)

    if csv_path.exists() == False:
        raise FileNotFoundError
    
    if len(csv_path.read_text(encoding = "utf-8")) <= 0:
        raise ValueError
    
    list_line_csv = []

    with csv_path.open('r',encoding = 'utf-8') as f:
        csv_read = csv.DictReader(f)
        for line in csv_read:
            list_line_csv.append(line)
    
    with json_path.open("w", newline = '', encoding = "utf-8") as f:
        json_writer = json.dump(list_line_csv,f,ensure_ascii=False, indent = 2)
        
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
```

![Картинка 1](./images/lab05/51.png)
![Картинка 2](./images/lab05/52.png)
![Картинка 3](./images/lab05/53.png)
![Картинка 4](./images/lab05/54.png)

### Задание номер 2

```python
import openpyxl
from pathlib import Path
import csv

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)

    if csv_path.exists() == False:
        raise FileNotFoundError
    
    if len(csv_path.read_text(encoding = "utf-8")) <= 0:
        return ""
    
    xlsx_book = openpyxl.Workbook()
    xlsx_sheet1 = xlsx_book.active
    xlsx_sheet1.title = "Sheet1"

    with csv_path.open('r',encoding = 'utf-8') as f:
        csv_read = csv.reader(f)
        
        for row in csv_read:
            xlsx_sheet1.append(row)


    xlsx_book.save(xlsx_path)
```