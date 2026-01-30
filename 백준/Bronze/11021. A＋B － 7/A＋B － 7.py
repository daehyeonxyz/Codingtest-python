import sys
input = sys.stdin.readline
output = sys.stdout.write

T = int(input())
for x in range(1, T+1):
    A, B = map(int, input().split())
    output(f"Case #{x}: {A+B}" + "\n")