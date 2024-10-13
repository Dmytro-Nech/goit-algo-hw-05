from pathlib import Path
import sys

# path = Path(sys.argv[1])

def parse_log_line(line: str) -> dict:
    list_log = line.split()
    dict_log = {}
    dict_log["Date"] = list_log[0]
    dict_log["Time"] = list_log[1]
    dict_log["Level"] = list_log[2]
    dict_log["Massage"] = " ".join(list_log[3:])
    return dict_log


def load_logs(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as file:
        parse_list = [parse_log_line(line) for line in file]
        return parse_list
    
def filter_logs_by_level(logs: list, level: str) -> list:
    result_list = []
    for el in logs:
        if level.upper() in el.values():
            result_list.append(f"{el["Date"]} {el["Time"]} - {el["Massage"]}")
    return result_list

def count_logs_by_level(logs: list) -> dict:
    count_dict = {}
    for el in logs:
        level = el.get("Level")
        if  level:
            if level in count_dict:
                count_dict[level] += 1
            else:
                count_dict[level] = 1
    return count_dict

def display_log_counts(counts: dict):
    pass



def main():
    listn = load_logs("log.txt")
    print(listn)
    print(filter_logs_by_level(listn, "INFO"))
    print(count_logs_by_level(listn))


if __name__ == "__main__":
    main()