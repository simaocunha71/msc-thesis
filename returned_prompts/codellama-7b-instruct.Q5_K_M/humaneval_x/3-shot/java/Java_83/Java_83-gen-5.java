        int result = 0;

        int end_digit = 10;
        int start_digit = 1;
        int end_count = 0;
        int start_count = 0;
        int current_digit = 0;

        while (end_digit >= start_digit) {
            end_count = (int) Math.pow(10, n - 1) / end_digit;
            start_count = (int) Math.pow(10, n - 1) / start_digit;
            current_digit = (int) Math.pow(10, n - 1) / end_digit;
            result += end_count + start_count - current_digit;

            end_digit /= 10;
            start_digit *= 10;
        }
        return result;
    }
}

