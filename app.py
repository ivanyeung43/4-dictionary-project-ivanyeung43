""" GPUs = [
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

for index, item in enumerate(GPUs):
    print(index, ":", item["name"])
shop = ""
cart = []
total = 0
while shop != "Checkout":
    user_purchase = input("Select one item to purchase: Type Checkout to end shopping")
    if user_purchase == "Checkout":
        print(cart)
        print(total)
    elif int(user_purchase) == 0:
        print(GPUs[0]["name"])
        cart.append(GPUs[0]["name"])
        total += GPUs[0]["price"]
    elif int(user_purchase) == 1:
        print(GPUs[1]["name"])
        cart.append(GPUs[1]["name"])
        total += GPUs[1]["price"]
    elif int(user_purchase) == 2:
        print(GPUs[2]["name"])
        cart.append(GPUs[2]["name"])
        total += GPUs[2]["price"]
print("Shopping has ended") """





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


def slot_m(q,m1,m2,m3):
    m1_played = 0
    m2_played = 0
    m3_played = 0
    while q > 0:
        q-1
        m1_played += 1
        if m1_played + m1 == 35:
            q+=30
        q-1
        m2_played += 1
        if m2_played + m2 == 100:
            q +=60
        q-1
        m3_played += 1
        if m3_played + m3 == 10:
            q +=9
        x = m1_played + m2_played + m3_played

    print(f"Martha plays {x} times before going broke")
slot_m(77, 4, 9, 3)
