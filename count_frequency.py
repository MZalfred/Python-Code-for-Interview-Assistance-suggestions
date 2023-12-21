# Count the frequency of each element in a list

def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

# Example usage
lst = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print("Frequency of each element:", count_frequency(lst))
