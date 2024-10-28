    def sum_of_binary(n):
        result = 0
        while n:
            result += n % 2
            n //= 2
        return result

    def to_binary(n):
        result = ""
        while n:
            result += str(n % 2)
            n //= 2
        return result

    result = to_binary(sum_of_binary(N))

    return result.zfill(4)



# def solve(N):
#     """Given a positive integer N, return the total sum of its digits in binary.
#     
#     Example
#         For N = 1000, the sum of digits will be 1 the output should be "1".
#         For N = 150, the sum of digits will be 6 the output should be "110".
#         For N = 147, the sum of digits will be 12 the output should be "1100".
#     
#     Variables:
#         @N integer
#          Constraints: 0 ≤ N ≤ 10000.
#     Output:
#          a string of binary number
#     """

#     if N == 0:
#         return "0000"
#     if N == 1:
#         return "0001"
#     if N == 2:
#         return "0010"
#     if N == 3:
#         return "0011"
#     if N == 4:
#         return "0100"
#     if N == 5:
#         return "0101"
#     if N == 6:
#         return "0110"
#     if N == 7:
#         return "0111"
#     if N == 8:
#         return "1000"
#     if N == 9:
#         return "1001"

#     if N % 2 == 0:
#         return str(solve(N//2)) + "0"
#