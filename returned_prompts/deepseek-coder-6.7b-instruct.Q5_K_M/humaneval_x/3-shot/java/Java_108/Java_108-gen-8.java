        int count = 0;
        for  (int num  : arr) {
            if  (sumDigits(num) > 0) count++;
        }
        return count;
    }

    private int sumDigits(int number)  {
        int sum = 0;
        while  (number != 0)  {
            sum += number % 10;
            number = number / 10;
        }
        return sum;
    }
}

