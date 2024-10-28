
    count := 0
    prime := [17]bool{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59}
    for _, c := range num {
        if i, _ := strconv.ParseInt(string(c), 16, 0); i > 0 {
            if prime[i] {
                count++
            }
        }
    }
    return count
}

// Tests
var (
    tests = []struct {
        num        string
        expected   int
    }{
        {
            "AB", 1,
        },
        {
            "1077E", 2,
        },
        {
            "ABED1A33", 4,
        },
        {
            "123456789ABCDEF0", 6,
        },
        {
            "2020", 2,
        },
    }
    for _, test := range tests {
        if actual := HexKey(test.num); actual != test.expected {
            t.Error("Expected", test.expected, "but got", actual)
        }
    }






























































































































































































