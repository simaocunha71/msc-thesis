        int count = 0;
        if(n == 1)
            return 2;
        if(n <= 0)
            return 0;
        else {
            count = (int) Math.pow(10, n-1) + startsOneEnds(n-1);
        }
        return count;
    }
}

This solution is not correct. The count of n-digit numbers that start or end with 1 is not equal to 10^(n-1) for n>1, because we have two cases: 1 at the start and 1 at the end. Therefore, we have to calculate it as 2 * 10^(n-1).

