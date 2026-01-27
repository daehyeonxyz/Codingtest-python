hour, min = map(int, input().split())
cook = int(input())

total = hour * 60 + min + cook
hour = (total // 60) % 24
min = total % 60

print(hour, min)