arr = list(map(int, input().split()))

if len(set(arr)) == 1:
    print(10000 + arr[0]*1000)
elif len(set(arr)) == 2:
    if arr[0] == arr[1] or arr[0] == arr[2]:
        print(1000 + arr[0]*100)
    else:
        print(1000 + arr[1]*100)
else:
    print(max(arr)*100)