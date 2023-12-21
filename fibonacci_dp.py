# Compute the nth Fibonacci number using dynamic programming

def fibonacci_dp(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

# Example usage
n = 10
print(f"Fibonacci number at position {n}:", fibonacci_dp(n))
