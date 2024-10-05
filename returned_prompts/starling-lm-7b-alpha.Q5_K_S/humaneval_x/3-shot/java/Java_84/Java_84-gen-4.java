        String result = "";
        int digit_sum = 0;
        while (N > 0) {
            digit_sum += N % 2;
            N = N / 2;
        }
        while (digit_sum > 0) {
            result += (digit_sum % 2 == 0 ? "0" : "1");
            digit_sum = digit_sum / 2;
        }
        return result;
    }
}

