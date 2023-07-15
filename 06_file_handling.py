# File Handling

import os

# .txt file

txt_file = open("my_file.txt", "r+")
# print(txt_file.read())

for line in txt_file.readlines():
    print(line)

print(txt_file.readline(2))

txt_file.write("\nAunque tambien me gusta Kotlin")
print(txt_file.readline())

# .json file

import json

json_file = open("my_file.json", "w+")

json_test = {
    "name": "Brais",
    "surname": "Moure",
    "age": 35,
    "languages": ["Python", "Swift", "Kotlin"],
    "website": "https://moure.dev"
}

json.dump(json_test, json_file, indent = 2)

json_file.close()

json_dict = json.load(open("my_file.json"))

# .cvs file

import csv

csv_file = open("my_file.csv", "w+")

csv_write = csv.writer(csv_file)
csv_write.writerow(["name", "surname", "age", "language", "website"])
csv_write.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])

csv_file.close()