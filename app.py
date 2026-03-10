items = [
    {
        "name": "RADEON XFX SWIFT RX 9070XT", 
        "price": 759.99, 
        "description": "325mm LENGTH," "16GB VRAM" "COLOR:BLACK/WHITE"
    },
    {
        "name": "NVIDIA FOUNDERS EDITION RTX 5070TI",
        "price": 849.99,
        "description": "305mm LENGTH," "16GB VRAM"  "COLOR:BLACK"
    },
    {
        "name": "GIGBYTE AORUS MASTER 5080",
        "price": 1199.99,
        "description": "360mm LENGTH, 16GB VRAM, COLOR:BLACK"
    },
]

for index, item in enumerate(items):
    print(index, ":", item["name"])
shop = ""
cart = []

while shop != "Checkout":
    user_purchase = input("Select one item to purchase: Type Checkout to end shopping")
    total = 0
    if user_purchase == "Checkout":
        print(cart)
        print(total)
    elif int(user_purchase) == 0:
        print(items[0]["name"])
        cart.append(items[0]["name"])
        total += items[0]["price"]
    elif int(user_purchase) == 1:
        print(items[1]["name"])
        total += items[1]["price"]
        cart.append(items[1]["name"])
    elif int(user_purchase) == 2:
        print(items[2]["name"])
        cart.append(items[2]["name"])
        total += items[2]["price"]
print("Shopping has ended")





""" # Practice Assessment
c = "c"
e = "."
def occupied(x,y,t):
    found = 0
    for i in range(x):
        if (y[i]) == c and t[i] == c:
            found += 1
    print(found)
            
occupied(5,[e,c,c,c,c], [c,c,c,c,e]) """


# Practice Asssessment #2

""" t = "t"
s = "s" 


def language(x):
    t_count = 0
    s_count = 0
    for i in range(len(x)):
        if (x[i]).lower() == t:
            t_count += 1
        elif (x[i]).lower() == s:
            s_count +=1
    if t_count > s_count:
        print("Enlgish")
    elif t_count == s_count:
        print("French")
    else:
        print("French")

language("This T t  tttttt") """
        


#Practice Test #3


""" def honi_track(sent):
    HONI = ["H", "O", "N", "I"]
    count = 0
    state = 0
    for char in sent:
        if HONI[state] == char.upper():
            state += 1
            if state >= 4:
                state = 0
                count += 1
    print(count)

honi_track("HHHHOOOONNNNIIII") """

