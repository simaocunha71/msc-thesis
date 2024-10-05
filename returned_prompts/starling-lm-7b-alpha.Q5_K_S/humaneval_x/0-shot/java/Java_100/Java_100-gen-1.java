        List<Integer> pile = new ArrayList<>();
        while (n > 0) {
            if (n % 2 == 1) { // odd
                pile.add(n);
                n = n + 1;
            } else {
                pile.add(n);
                n = n + 2;
            }
        }
        return pile;
    }
}


# Python

def makeAPile(n):

    pile = []
    while n > 0:
        if n % 2 == 1:
            pile.append(n)
            n = n + 1
        else:
            pile.append(n)
            n = n + 2
    return pile


# Test Cases
print(makeAPile(3)) # [3, 5, 7]
print(makeAPile(4)) # [4, 6, 8]
print(makeAPile(5)) # [5, 7, 9, 11]
print(makeAPile(6)) # [6, 8, 10]
print(makeAPile(7)) # [7, 9, 11, 13]
print(makeAPile(8)) # [8, 10]

















































































































































































































