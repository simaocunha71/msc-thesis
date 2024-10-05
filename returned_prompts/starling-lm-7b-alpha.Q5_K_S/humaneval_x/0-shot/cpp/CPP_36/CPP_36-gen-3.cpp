    int count = 0;
    for (int i = 11; i < n; i += 11) {
        if (i % 13 == 0) {
            if (i % 10 == 7)
                count++;
        }
    }
    for (int i = 13; i < n; i += 13) {
        if (i % 11 == 0) {
            if (i % 10 == 7)
                count++;
        }
    }
    return count;
}

/*
Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
>>> fizz_buzz(50)
0
>>> fizz_buzz(78)
2
>>> fizz_buzz(79)
3
*/
int fizz_buzz(int n) {
    int count = 0;
    for (int i = 11; i < n; i += 11) {
        if (i % 13 == 0) {
            if (i % 10 == 7)
                count++;
        }
    }
    for (int i = 13; i < n; i += 13) {
        if (i % 11 == 0) {
            if (i % 10 == 7)
                count++;
        }
    }
    return count;
}




























































































































































