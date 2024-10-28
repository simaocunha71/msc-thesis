        int sum = 0;
        for (int i = 0; i < Math.min(arr.size(), k); i++) {
            int digit = arr.get(i);
            if (digit >= 10) {
                sum += digit % 10;
            } else {
                sum += digit;
            }
        }
        return sum;
    }
}

