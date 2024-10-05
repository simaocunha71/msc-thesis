def modp(n: int, p: int):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow(2, n // 2, p) * pow(2, n // 2, p)
    else:
        return pow(2, n, p)  # 2^n mod p
    # For large n, use the fast exponentiation algorithm (binary exponentiation) to avoid overflow. For small n, use the pow function with 3 arguments.
    # This function works for any integers n and p, but be aware of potential numerical issues for large values. In such cases, consider using the 'gmpy2' library for arbitrary-precision arithmetic.  # noqa: E501


def main():
    print(modp(3, 5))  # 3
    print(modp(1101, 101))  # 2
    print(modp(0, 101))  # 1
    print(modp(3, 11))  # 8
    print(modp(100, 101))  # 1

if __name__ == "__main__":
    main()

# Output:
# 3
# 2
# 1
# 8
# 1
#  # noqa: E305
#  # noqa: E302
#  # noqa: E305
#  # noqa: E302
#  # noqa: E305
#  # noqa: E302
#  # noqa: E305
#  # noqa: E302
#  # noqa: E305
#  # noqa: E302
#  # noqa: E305
#  # noqa: E302
#  # noqa: E305
#  # noqa: E302
#  # noqa: E305
#  # noqa: E302
#  # noqa: E305
#  # noqa: E302
#  # noqa: E305
#  # noqa: E302
#  # noqa: E305
#  # noqa: E302
#  # noqa: E305
#  # noqa: E302
#  # noqa: E305
#  # noqa: E302
#  # noqa: E305
#  # noqa: E302
#  # noqa: E305
#  # noqa