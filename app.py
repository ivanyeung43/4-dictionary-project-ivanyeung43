item = [
    {
        "name": "RADEON XFX SWIFT RX 9070XT", 
        "price": 829.99, 
        "description": "325mm LENGTH," "16GB VRAM" "COLOR:BLACK/WHITE"
    },
    {
        "name": "NVIDIA FOUNDERS EDITION RTX 5070TI",
        "price": 929.99,
        "description": "304mm LENGTH, 16GB VRAM, COLOR:BLACK"
    },
    {
        "name":"GIGABYTE AOROUS MASTER RTX 5080",
        "price": 1299.99,
        "description": "360mm LENGTH, 16GB VRAM, COLOR:BLACK"
    },
]


for index, item in enumerate(item):
    print(index, ":", item["name"])

user_purchase = input("Select one item to purchase")

if user_purchase == "0":
    item[0]["name"]
elif user_purchase == "1":
    item[1]["name"]
elif user_purchase == "2":
    item[2]["name"]
else:
    print("Select 0, 1 or 2")

