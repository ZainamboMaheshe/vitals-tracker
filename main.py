
from pathlib import Path

folder = Path(__file__).resolve().parent
filename = folder / "vitals.csv"


name = input("Enter test resident name: ")

systolic = int(input("Systolic BP: "))
diastolic = int(input("Diastolic BP: "))
heart_rate = int(input("Heart rate: "))
temperature = float(input("Temperature (F): "))

print("Vitals entered successfully!")

flags = []

if systolic < 90 or systolic > 120:
    flags.append("Systolic BP outside example range")

if diastolic < 60 or diastolic > 80:
    flags.append("Diastolic BP outside example range")

if heart_rate < 60 or heart_rate > 100:
    flags.append("Heart rate outside example range")

if temperature < 97 or temperature > 99:
    flags.append("Temperature outside example range")

if flags:
    print("Flags:")
    for flag in flags:
        print("-", flag)
else:
    print("No values flagged")

import csv

with open(filename, "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        name,
        systolic,
        diastolic,
        heart_rate,
        temperature
    ])

print("Vitals saved successfully!")


