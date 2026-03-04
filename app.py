""" item = [
    {
        "name": "RADEON XFX SWIFT RX 9070XT", 
        "price": "$729.99", 
        "description": "325mm LENGTH," "16GB VRAM" "COLOR:BLACK/WHITE"
    },
    {
        "name": "NVIDIA FOUNDERS EDITION RTX 5070TI",
        "price": "$749.99",
        "description": "305mm LENGTH," "16GB VRAM"  "COLOR:BLACK"
    },
    {
        "name": "GIGBYTE AORUS MASTER 5080",
        "price": "$1299.99",
        "description": "360mm LENGTH, 16GB VRAM, COLOR:BLACK"
    },
]


for index, item in enumerate(item):
    print(index, ":", item["price"])


user_purchase = int(input("Select one item to purchase"))
 """




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
h = "h"
o = "o"
n = "n"
i = "i"
def honi_track(sent):
    x = sent.split()
    honi_amount = 0
    search_term = h
    for letter in range(len(x)):
        if x[letter] == search_term:
            honi_amount += 0.25

    print(honi_amount)
honi_track("HONI")