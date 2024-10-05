        int count = 0;
        for (int num : arr) {
            if (num > 0) {
                int sum = 0;
                for (int digit : String.valueOf(Math.abs(num)).chars().map(c -> c - '0').boxed().toList()) {
                    sum += digit;
                }
                if (sum > 0) {
                    count++;
                }
            }
        }
        return count;
    }
}

