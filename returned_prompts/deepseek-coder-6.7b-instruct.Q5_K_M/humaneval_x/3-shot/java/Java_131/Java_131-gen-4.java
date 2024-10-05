        int product = 1;
        boolean isOdd  found = false;

        while  (n > 0)  {
            int digit = n % 10;
            if  (digit % 2 != 0)  {
                product *= digit;
                found = true;
            }
            n /= 10;
        }

        return found ? product : 0;
    }
}

