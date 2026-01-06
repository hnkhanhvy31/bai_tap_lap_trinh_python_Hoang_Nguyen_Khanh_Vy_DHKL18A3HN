import json
from collections import Counter

with open("employees.json", "r", encoding="utf-8") as f:
    data = json.load(f)

employees = data["employees"]
total = len(employees)

counter = Counter(emp["unit"] for emp in employees)

print("Tên công ty:", data["company"]["name"])
print("Địa chỉ:", data["company"]["address"])
print("----- Thống kê nhân viên theo đơn vị -----")

i = 1
for unit, count in counter.items():
    percent = count / total * 100
    print(f"{i}. Tên đơn vị: {unit}")
    print(f"   - Số nhân viên: {count}")
    print(f"   - Tỷ lệ: {percent:.2f}%")
    i += 1
