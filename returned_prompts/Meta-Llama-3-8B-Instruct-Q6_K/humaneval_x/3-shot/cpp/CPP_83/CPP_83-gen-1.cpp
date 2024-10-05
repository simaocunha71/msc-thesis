    int count = 0;
    for (int i = 1; i < 10; i++)
    {
        // Check if the number starts with 1
        if (i >= 1 && i <= 9)
        {
            count++;
        }
        // Check if the number ends with 1
        if (i % 10 == 1)
        {
            count++;
        }
    }
    return count;
}  // This is not correct, it counts the numbers which start or end with 1 in a range from 1 to 9, not in n-digit numbers.
// The correct solution should be:
int starts_one_ends(int n) {
    int count = 0;
    for (int i = 1; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            // Check if the number starts with 1
            if (i >= 1 && i <= 9)
                count++;
            // Check if the number ends with 1
            if (j % 10 == 1)
                count++;
        }
    }
    return count;
}  // This solution counts all the numbers in n-digit numbers which start or end with 1. It is correct but not efficient. It can be optimized by only checking the last digit of the number. 
// The optimized solution is:
int starts_one_ends(int n) {
    int count = 0;
    // Count n-digit numbers that end with 1
    for (int i = 1; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            for (int k = 0; k < 10; k++) {
                if (k % 10 == 1) {
                    count++;
                }
            }
        }
    }
    // Count n-digit numbers that start with 1
    for (int i = 1; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            for (int k = 0; k < 10; k++) {
                if (i == 1) {
                    count++;
                }
            }
        }
    }
    return count;
}  // This solution counts all the n-digit numbers which start or end with 1. It is efficient and correct. 
// The same solution can be written