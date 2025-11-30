# Method 1: Using exponent operator
def power2_a(n):
    return 2 ** n


# Method 2: Iterative approach (while loop)
def power2_b(n):
    result = 1
    i = 0
    while i < n:
        result *= 2    # multiply result by 2 each step
        i += 1
    return result


# Method 3: Recursive (divide & conquer)
def power2_c(n):
    if n == 0:
        return 1
    if n % 2 == 0:         # if n is even
        half = power2_c(n // 2)
        return half * half
    else:                  # if n is odd
        return 2 * power2_c(n - 1)


# Method 4: Bit shifting (1 shifted left by n bits)
def power2_d(n):
    return 1 << n



if __name__ == "__main__":
    n = 10

    print("power2_a:", power2_a(n))
    print("power2_b:", power2_b(n))
    print("power2_c:", power2_c(n))
    print("power2_d:", power2_d(n))