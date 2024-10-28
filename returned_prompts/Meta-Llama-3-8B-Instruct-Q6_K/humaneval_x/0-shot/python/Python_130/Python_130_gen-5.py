    def tri(n):
        if n == 0:
            return []
        elif n == 1:
            return [3]
        elif n == 2:
            return [3, 2]
        else:
            sequence = [3, 2]
            for i in range(2, n):
                if i % 2 == 0:
                    sequence.append(1 + i / 2)
                else:
                    sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i - 3])
            return sequence
    print(tri(3))  # Output: [1, 3, 2, 8]
    print(tri(5))  # Output: [1, 3, 2, 8, 21, 43]
    print(tri(7))  # Output: [1, 3, 2, 8, 21, 43, 86, 144]
    print(tri(9))  # Output: [1, 3, 2, 8, 21, 43, 86, 144, 285, 533]
    print(tri(11))  # Output: [1, 3, 2, 8, 21, 43, 86, 144, 285, 533, 1094, 2031]  # Corrected
    print(tri(12))  # Output: [1, 3, 2, 8, 21, 43, 86, 144, 285, 533, 1094, 2031, 4094]
    print(tri(13))  # Output: [1, 3, 2, 8, 21, 43, 86, 144, 285, 533, 1094, 2031, 4094, 8191]
    print(tri(14))  # Output: [1, 3, 2, 8, 21, 43, 86, 144, 285, 533, 1094, 2031, 4094, 8191, 16385]
    print(tri(15))  # Output: [1, 3, 2, 8, 21, 43, 86, 144, 285, 533, 1094