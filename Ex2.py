# x = int(input("Введите X: "))
# y = int(input("Введите Y: "))
# z = int(input("Введите Z: "))
# left = not (x or y or z)
# right = not x and not y and not z   
# if left == right:
#         print("Утверждение истинно")
# else:
#         print("Утверждение ложно")
def Numbers(x):
    xyz = ["X", "Y", "Z"]
    n = []
    for i in range(x):
        n.append(input(f"Введите {xyz[i]}: "))
    return n
x = Numbers(3)
left = not (x[0] or x[1] or x[2])
right = not x[0] and not x[1] and not x[2]     
if left == right:
        print("Утверждение истинно")
else:
        print("Утверждение ложно")

