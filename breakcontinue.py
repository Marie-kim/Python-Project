#Break statement - Exits an entire loop

num = 20
while num <= 25:
    print(num)
    if num == 23:
        break
    num += 1

#continue statement - Skips a loop
devices = ["laptop", "phone", "tablet"]
for x in devices:
    if x == "phones":
        continue
        print(x)


