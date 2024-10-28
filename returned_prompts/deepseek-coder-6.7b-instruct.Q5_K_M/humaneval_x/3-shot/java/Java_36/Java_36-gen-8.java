        int count = 0;
        for  (int i = 11; i < n; i += 11) {
            count += countDigits(i, 7);
        }

        for  (int i = 13; i < n; i += 13) {
            count += countDigits(i, 7);
        }

        return count;
    }

    private int countDigits(int num, int digit) {
        int count = 0;
        while  (num  != 0)  {
            if  (num  % 10 == digit)  {
                count++;
            }
            num  /= 10;
        }
        return count;
    }
}

