        int result = 0;
        for (int value : arr) {
            int sum = 0;
            while (value != 0) {
                sum += Math.abs(value % 10);
                value /= 10;
            }
            if (sum > 0) result += 1;
        }
        return result;
    }
}

