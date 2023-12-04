import csv


def write_to_csv(file_name, data):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        # 写入标题头（如果需要的话）
        writer.writerow(['Result', "Difficulty", "DoWhat", "Before", "After"])
        # 写入数据
        for row in data:
            writer.writerow(row)