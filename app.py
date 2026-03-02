""" item = [
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

user_purchase = int(input("Select one item to purchase")) """




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

t = "t"
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

language("This T t  tttttt")
        


