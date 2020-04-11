# 6.089%{content: "Graphic|";}

skills = [
    "Web Developer",
    "IOT Developer",
    "Freelancer"
]

list = []

for element in skills:
    word = ""
    for char in element:
        word = word + char
        dis = "{content: \"" + word + "|\";}"
        list.append(dis)

    for char in word:
        word = word[:len(word)-1]
        dis = "{content: \"" + word + "|\";}"
        list.append(dis)

d = 100.00/len(list)

p = 0
for element in list:
    p = p + d
    p = round(p, 2)
    final = str(p) + "%" + element
    print(final)
