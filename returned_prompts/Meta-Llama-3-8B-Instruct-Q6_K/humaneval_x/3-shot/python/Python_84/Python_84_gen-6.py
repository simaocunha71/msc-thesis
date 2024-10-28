    def get_binary_sum(n):
        total_sum = 0
        while n > 0:
            total_sum += n % 2
            n //= 2
        return total_sum

    return bin(get_binary_sum(N))[2:]  # remove '0b' prefix


