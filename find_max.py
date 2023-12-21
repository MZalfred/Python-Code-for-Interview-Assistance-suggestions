# Find the maximum element in an array

def find_max(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

# Example usage
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("Maximum value:", find_max(arr))
