
n = int(input())
for i in range(1, n+1):
    print(i, end=" ")
    for j in range(i):
        print("#", end="")
    print()
