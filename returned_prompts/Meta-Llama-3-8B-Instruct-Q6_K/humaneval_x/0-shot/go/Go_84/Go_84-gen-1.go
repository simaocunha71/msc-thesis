var sum int
var binary string
for N > 0 {
    remainder := N % 2
    if remainder == 1 {
        sum++
    }
    N = N / 2
    binary = strconv.Itoa(remainder) + binary
}
return strconv.Itoa(sum) + "b"

}

// Test your function with the following test cases:
// Solve(1000) should return "1"
// Solve(150) should return "110"
// Solve(147) should return "1100"
// Solve(1) should return "1"
// Solve(10) should return "1"
// Solve(20) should return "1"
// Solve(100) should return "1"
// Solve(1000) should return "1"
// Solve(2000) should return "1"
// Solve(10000) should return "1"
// Solve(10001) should return "1"
// Solve(10000) should return "1"
// Solve(0) should return "0"
// Solve(1) should return "1"
// Solve(2) should return "1"
// Solve(3) should return "1"
// Solve(4) should return "1"
// Solve(5) should return "1"
// Solve(6) should return "1"
// Solve(7) should return "1"
// Solve(8) should return "1"
// Solve(9) should return "1"
// Solve(10) should return "1"
// Solve(11) should return "1"
// Solve(12) should return "1"
// Solve(13) should return "1"
// Solve(14) should return "1"
// Solve(15) should return "1"
// Solve(16) should return "1"
// Solve(17) should return "1"
// Solve(18) should return "1"
// Solve(19) should return "1"
// Solve(20) should return "1"
// Solve(21) should return "1"
// Solve(22) should return "1"
// Solve(23) should return "1"
// Solve(24) should return "1"
// Solve(25) should return "1"
// Solve(26) should return "1"
// Solve(27) should return "1"
// Solve(28) should return "1"
// Solve(29) should return "1"
// Solve(30) should return "1"
//