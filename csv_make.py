import csv
file_path = "test_csv.csv"
data = []
# 出来高を足すためのリストを作成
sum = 0

with open(file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)
        sum += int(row['出来高'])

print(sum)
print(data)
