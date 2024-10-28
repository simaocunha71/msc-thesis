    binary_list = []
    while N:
        binary_list.append(N % 2)
        N = N // 2
    binary_list.reverse()

    sum_list = [sum(binary_list[:i+1]) for i in range(len(binary_list))]
    binary_list = ["1"]*sum_list[0] + ["0"]*(len(binary_list)-sum_list[0]) + "0"
    for i in range(len(sum_list)-1):
        binary_list = ["1"]*sum_list[i+1] + ["0"]*(len(binary_list)-sum_list[i+1]) + "0"
    return "".join(binary_list)



# Test cases
assert solve(1000) == "1"
assert solve(150) == "110"
assert solve(147) == "1100"
assert solve(0) == "0"
assert solve(1) == "1"
assert solve(2) == "10"
assert solve(3) == "11"
assert solve(4) == "100"
assert solve(5) == "101"
assert solve(6) == "110"
assert solve(7) == "111"
assert solve(8) == "1000"
assert solve(9) == "1001"
assert solve(10) == "1010"
assert solve(11) == "1011"
assert solve(12) == "1100"
assert solve(13) == "1101"
assert solve(14) == "1110"
assert solve(15) == "1111"
assert solve(20) == "10100"
assert solve(21) == "10101"
assert solve(22) == "10110"
assert solve(23) == "10111"
assert solve(24) == "11000"
assert solve(25) == "11001