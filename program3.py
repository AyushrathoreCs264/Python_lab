arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr[k - 1])

