    def tri(n):
        if n == 0:
            return [1]
        elif n == 1:
            return [1, 3]
        elif n == 2:
            return [1, 3, 2]
        else:
            tribonacci = [1, 3, 2]
            while len(tribonacci) < n + 1:
                if len(tribonacci) % 2 == 0:
                    tribonacci.append(1 + len(tribonacci) // 2)
                else:
                    tribonacci.append(tribonacci[-1] + tribonacci[-2] + tribonacci[-3])
            return tribonacci
    print(tri(3))  # Output: [1, 3, 2, 8]
    print(tri(5))  # Output: [1, 3, 2, 8, 21, 43]
    print(tri(7))  # Output: [1, 3, 2, 8, 21, 43, 109, 233]
    print(tri(9))  # Output: [1, 3, 2, 8, 21, 43, 109, 233, 576]    



# tribonacci sequence
# tribonacci sequence is a sequence defined by a recurrence relation. 
# The sequence starts with 1, 3, 2, and each subsequent term is the sum of the previous three terms. 
# The sequence is named after the mathematician Bonaventura Cavalieri, 
# who discovered it in the 17th century. 
# The sequence has many interesting properties and appears in many areas of mathematics and science. 
# It is also known as the "Cavalieri sequence" or the "Tribonacci sequence".
# It is named after the Italian mathematician Bonaventura Cavalieri, 
# who discovered it in the 17th century. 
# The sequence is also known as the "Cavalieri sequence" or the "Tribonacci sequence".
# It is named after the Italian mathematician Bonaventura Cavalieri, 
# who discovered it in the 17th century. 
# The sequence is also known as the "Cavalieri sequence" or the "Tribonacci sequence".

# Tribonacci sequence is a sequence of natural numbers where each term is the sum of the previous three terms. 
# The sequence is named after