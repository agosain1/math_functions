numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def insert(fofx, x):
    temp = fofx.split(" ")
    f = []
    y = []
    for i in range (0, len(temp)):
        f.append(temp[i].split("^"))
    for terms in range (0, len(f), 2):
        a = f[terms] #Term #1
        if len(a)> 1 and a[0] != "x":
            for i in range (0, len(a)):
                a[i] = a[i].replace("x", "")
            if len(f) > 1 and terms > 1:
                y.append(float(f[terms - 1][0] + str(float(a[0]) * (x ** float(a[1])))))
            else:
                y.append(float(a[0]) * (x ** float(a[1])))
        elif a[0] == "x":
            if len(f)> 1 and terms > 1:
                y.append(float(f[terms - 1][0] + str(x)))
            else:
                y.append(x)
        elif a[0][0] in numbers and "x" in a[0]:
            if len(f) > 1 and terms > 1:
                y.append(float(f[terms - 1][0] + str(x * float((a[0].replace("x", ""))))))
            else:
                y.append(x * float((a[0].replace("x", ""))))
        else:
            if len(f) > 1 and terms > 1:
                y.append(float(f[terms - 1][0] + a[0]))
            else:
                y.append(float(a[0]))
    print(sum(y))
    return(sum(y))

def integral(t1, t2):
    return(insert(func, t2) - insert(func, t1))
#Evaluate a function f(x) based on an inputted value x.
func = input("f(x) = ")
t1 = float(input("t1 = "))
t2 = float(input("t2 = "))
print(integral(t1, t2))
