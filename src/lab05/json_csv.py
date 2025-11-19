import csv
import json
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    json_path = Path(json_path)

    if not json_path.exists():
        raise FileNotFoundError

    with json_path.open("r", encoding="utf-8") as f:
        try:
            json_import = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Некорректный JSON")

    if not json_import:
        raise ValueError("JSON файл пуст")

    csv_path = Path(csv_path)

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        csv_writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
        csv_writer.writeheader()
        csv_writer.writerows(json_import)


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_path = Path(csv_path)
    json_path = Path(json_path)

    if not csv_path.exists():
        raise FileNotFoundError

    list_line_csv = []

    with csv_path.open("r", encoding="utf-8") as f:
        csv_read = csv.DictReader(f)
        for line in csv_read:
            list_line_csv.append(line)

    if not list_line_csv:
        raise ValueError("CSV файл не содержит данных")

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(list_line_csv, f, ensure_ascii=False, indent=2)
