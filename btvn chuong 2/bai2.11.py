import json
from datetime import datetime

transactions = []

while True:
    money = input("Nhập số tiền giao dịch (hoặc 0 để dừng): ")
    if money == "0":
        break
    gold = input("Nhập số lượng vàng: ")
    transactions.append({
        "money": money,
        "gold": gold
    })

choice = input("Ghi vào file? (1: Có, 0: Không): ")

if choice == "1":
    filename = datetime.now().strftime("%Y-%m-%d-%H-%M-%S.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(transactions, f, indent=4, ensure_ascii=False)
    print("Đã ghi file:", filename)
else:
    print("Không ghi file")