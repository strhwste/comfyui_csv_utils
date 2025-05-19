# comfyui-csv-utils

Row‑based CSV utilities for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

## 🚀 Features

- **Search CSV by Row**  
  Reads a value from a specific row and column (identified by header).

- **Write CSV by Row**  
  Writes a value to a specific row and column (identified by header), extending rows/columns as needed.

## 📂 Installation

From your ComfyUI directory:

```bash
git clone https://github.com/strhwste/comfyui_csv_utils
```
Then restart ComfyUI.

## 🛠 Usage
In ComfyUI’s node browser, navigate to utils > csv.

Drag in Search CSV by Row or Write CSV by Row.

Set:

Path: Full path to your CSV file.

Row: 1‑based row index (header is row 0).

Header: Column name.

Value (for write): The string to write.

## 📖 Examples
Given a file data.csv:

csv
Copy
Edit
Keyword;Name;Age
row1;Alice;30
row2;Bob;25
Search CSV by Row

Inputs: Path="data.csv", Row=2, Header="Name"

Output: "Bob"

Write CSV by Row

Inputs: Path="data.csv", Row=3, Header="Age", Value="35"

Resulting data.csv:

csv
Copy
Edit
Keyword;Name;Age
row1;Alice;30
row2;Bob;25
; ;35

## 📜 License
This project is released under the MIT License. See LICENSE for details.

