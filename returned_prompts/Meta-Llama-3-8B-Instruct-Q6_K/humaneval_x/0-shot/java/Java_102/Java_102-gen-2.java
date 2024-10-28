    public int chooseNum(int x, int y) {
        if (x > y) {
            int temp = x;
            x = y;
            y = temp;
        }
        for (int i = x; i <= y; i++) {
            if (i % 2 == 0) {
                return i;
            }
        }
        return -1;
    }  // return the biggest even number in the range [x, y] inclusive

    // if there's no such number, return -1
    // if x is greater than y, swap them to ensure x is smaller or equal to y

    // check each number in the range [x, y] to see if it's even
    // if it's even, return it as the biggest even number in the range
    // if no even number is found in the range, return -1


