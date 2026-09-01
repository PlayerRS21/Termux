import os
x=os.listdir(path=".")

for i in range(len(x)):
    if x[i].endswith(".png"):
        os.remove(f"{x[i]}")
print("done")
