        int sum = 0;
        String result = "";
        while (N > 0) {
            sum += N % 2;
            N = N >> 1;
        }
        while (sum > 0) {
            result = Integer.toString(sum % 2) + result;
            sum /= 2;
        }
        return result;
    }
}

