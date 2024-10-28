    return pow(n, p-2, p)
    # This is the standard method for modular exponentiation. It uses the property of modular arithmetic
    # that a^(p-1) % p = 1. So, we raise n to the power of p-2 and then take the remainder when divided by p.
    # This is more efficient than repeatedly multiplying n by itself, especially for large values of n and p.
    # Note that this method is not suitable for all values of n and p, as it requires that p be prime and that n be relatively prime to p.
    # In the case where p is not prime, we would need to use a different method, such as the extended Euclidean algorithm.
    # Similarly, if n is not relatively prime to p, we would need to use a different method, such as the Chinese remainder theorem.
    # But for the typical case where n and p are relatively prime and p is prime, this method is efficient and accurate.
    # It's also worth noting that this method is not suitable for cryptographic purposes, as it is not secure.
    # For cryptographic purposes, you would need to use a more secure method, such as the Montgomery ladder or the sliding window algorithm.
    # These methods are more complex and require more computational resources, but they are more secure and can be used for cryptographic purposes.