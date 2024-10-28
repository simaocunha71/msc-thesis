        int result = 0;
        for (int n : arr) {
            int sum = 0;
            while (n != 0) {
                sum += Math.abs(n % 10);
                n /= 10;
            }
            if (sum > 0) result += 1;
        }
        return result;
    }
}

