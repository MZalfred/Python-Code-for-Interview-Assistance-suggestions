# Calculate the nth Fibonacci number

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
n = 5
print(f"Fibonacci number at position {n}:", fibonacci(n))
