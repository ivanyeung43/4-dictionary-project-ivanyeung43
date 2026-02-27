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
    item[0]["name"]["price"]
elif user_purchase == "1":
    item[1]["name"]["price"]
elif user_purchase == "2":
    item[2]["name"]["price"]
else:
    print("Select 0, 1 or 2")


""" # Practice Assessment
c = "c"
e = "."
def occupied(x,y,t):
    found = 0
    for i in range(x):
        if (y[i]) == c and t[i] == c:
            found += 1
    print(found)
            
occupied(5,[e,c,c,c,c], [c,c,c,c,e])
 """
