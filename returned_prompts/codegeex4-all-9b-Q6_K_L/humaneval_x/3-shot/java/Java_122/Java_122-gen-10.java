        int sum = 0;
        for (int i = 0; i < k; i++) {
            int element = arr.get(i);
            int first_digit = element % 10;
            int second_digit = (element / 10) % 10;
            sum += first_digit + second_digit;
        }
        return sum;
    }
}

