

    def modp(n: int, p: int):
        if n == 0:
            return 1
        elif n == 1:
            return 2
        else:
            half_n = modp(n // 2, p)
            if n % 2 == 0:
                return (half_n ** 2) % p
            else:
                return ((half_n ** 2) * 2) % p


print(modp(1101, 101))



#  In this function we are using the mathematical property that if a^n = (a^2)^(n/2)
#  and if n is even then we can simply use this property and if n is odd then we need to multiply the result by a (in this case a is 2).
#  We also need to handle the case where n is 0 and n is 1 separately as they are base cases.
#  We also need to take modulo p at every step to avoid overflow.

#  Note: This function assumes that p is a prime number and n is a non-negative integer.
#  If p is not a prime number, the result will be incorrect.
<jupyter_output>
2
<jupyter_text>
