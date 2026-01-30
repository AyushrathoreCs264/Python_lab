arr = [1, 4, 3, 5, 8, 6]

largest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]
print(largest)

