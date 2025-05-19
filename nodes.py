import csv
import os

class SearchCSVByRow:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Path": ("STRING", {"default": ""}),
                "Row": ("INT", {"default": 1, "min": 1}),
                "Header": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Value",)
    FUNCTION = "search_csv_by_row"
    CATEGORY = "utils/csv"

    def search_csv_by_row(self, Path, Row, Header):
        if not os.path.exists(Path):
            print(f"Error: Die Datei {Path} existiert nicht.")
            return ("",)
        with open(Path, mode='r', newline='', encoding='utf-8', errors='replace') as csvfile:
            rows = list(csv.reader(csvfile, delimiter=';'))
        if not rows:
            print("Error: Die CSV-Datei ist leer.")
            return ("",)
        header_row = rows[0]
        if Header not in header_row:
            print(f"Error: Header '{Header}' nicht gefunden.")
            return ("",)
        col_index = header_row.index(Header)
        if Row < 1 or Row >= len(rows):
            print(f"Error: Row-Index {Row} außerhalb (1–{len(rows)-1}).")
            return ("",)
        row = rows[Row]
        return (row[col_index] if col_index < len(row) else "",)

class WriteCSVByRow:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Path": ("STRING", {"default": ""}),
                "Row": ("INT", {"default": 1, "min": 1}),
                "Header": ("STRING", {"default": ""}),
                "Value": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("WrittenValue",)
    FUNCTION = "write_csv_by_row"
    CATEGORY = "utils/csv"

    def write_csv_by_row(self, Path, Row, Header, Value):
        rows = []
        if os.path.exists(Path):
            with open(Path, mode='r', newline='', encoding='utf-8', errors='replace') as csvfile:
                rows = list(csv.reader(csvfile, delimiter=';'))
        if not rows:
            rows = [["Keyword"]]
        header_row = rows[0]
        if Header not in header_row:
            header_row.append(Header)
            for r in rows[1:]:
                r.append("")
        col_index = header_row.index(Header)
        # sicherstellen, dass die Zeile existiert
        while len(rows) <= Row:
            rows.append([""] * len(header_row))
        # sicherstellen, dass jede Zeile lang genug ist
        for r in rows:
            while len(r) < len(header_row):
                r.append("")
        # Wert schreiben
        rows[Row][col_index] = Value
        # speichern
        with open(Path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerows(rows)
        return (Value,)
