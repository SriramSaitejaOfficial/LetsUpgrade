x = []
n = input("enter length")
for i in range(0, int(n)):
    k=input("enter value")
    x.append(int(k))

for i in range(0, int(n)):
    if x[i]%3==0:
        print(x[i])
    else:
        continue