index = 0
m = 0
for i in range(1, 10):
    A = int(input())
    if (A > m):
        m = A
        index = i
print(m)
print(index)