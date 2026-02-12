_, X = map(int, input().split())
A = map(int, input().split())
print(*(i for i in A if i < X))