import csv
import random
import time

x_value = 0
total_1 = 1000
total_2 = 1000

fieldnames = ["x_value", "total_1", "total_2"]

with open("data_gen.csv", "w") as file:
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open("data_gen.csv", "a") as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

        info = {"x_value": x_value, "total_1": total_1, "total_2": total_2}

        csv_writer.writerow(info)
        print(f"{x_value} {total_1} {total_2}")

        x_value += 1
        total_1 += random.randint(-6, 8)
        total_2 += random.randint(-5, 6)

    time.sleep(1)
