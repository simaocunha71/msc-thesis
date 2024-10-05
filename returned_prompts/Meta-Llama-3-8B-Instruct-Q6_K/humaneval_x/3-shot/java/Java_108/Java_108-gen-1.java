        int count = 0;
        for (int num : arr) {
            if (Math.abs(num) > 0) {
                int sum = 0;
                while (Math.abs(num) > 0) {
                    sum += Math.abs(num) % 10;
                    num /= 10;
                }
                if (sum > 0) {
                    count++;
                }
            }
        }
        return count;
    }
}

