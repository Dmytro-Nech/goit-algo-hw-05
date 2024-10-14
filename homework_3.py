from collections import defaultdict
from pathlib import Path
import sys

# Перевірка кількості аргументів командної строки
if len(sys.argv) < 2:
    print("Будь ласка, вкажіть шлях до директорії як аргумент.")
    sys.exit(1)

path = Path(sys.argv[1]) 

# Парсинг строки
def parse_log_line(line: str) -> dict:
    try:
        list_log = line.split()
        dict_log = {
            "Date" : list_log[0],
            "Time" : list_log[1],
            "Level" : list_log[2],
            "Massage" : " ".join(list_log[3:])
        }
        
        return dict_log
    except IndexError:
        print("Невірний формат файлу, або файл пошкоджено!")
        return None

# Завантаження логів із файла
def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            parse_list = [parse_log_line(line) for line in file]
        return parse_list
    except FileNotFoundError:
        print("Файл не знайдено")
        sys.exit(1)

# Фільтрація логів по рівню
def filter_logs_by_level(logs: list, level: str) -> list:
    result_list = []
    for el in logs:
        if level.upper() in el.values():
            result_list.append(f"{el["Date"]} {el["Time"]} - {el["Massage"]}")
    return result_list

#  підрахунок кількості логів по рінвям
def count_logs_by_level(logs: list) -> dict:
    count_dict = defaultdict(int)
    for el in logs:
        level = el.get("Level")
        if level:
            count_dict[level] += 1
    return count_dict

# Відображення таблиці логів
def display_log_counts(counts: dict):
    header = "{:<20}|{:<20}".format("Рівень логування", "Кількість")
    separator = "-"*len(header)
    insert = ""
    for key, value in counts.items():
        insert += "{:<20}|{:<20}\n".format(key, value)
    table = "\n".join([header, separator, insert.strip()])
    print(table)


def main():    
    list_of_logs = load_logs(path)
    
    # Підрахунок логів та відображення результатів
    table = count_logs_by_level(list_of_logs)
    display_log_counts(table)
    
    # Якщо преданий 2й аргумет в командній строці
    if len(sys.argv) > 2:
        level = sys.argv[2]
        print(f"\nДеталі логів для рівня {level.upper()}:")
        filtered_logs = filter_logs_by_level(list_of_logs, level)
        for log in filtered_logs:
            print(log)

if __name__ == "__main__":
    main()