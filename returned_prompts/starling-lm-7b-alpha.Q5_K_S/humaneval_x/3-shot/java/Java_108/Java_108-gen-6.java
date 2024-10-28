        int count = 0;
        for (int x : arr) {
            int sum = 0;
            while (x != 0) {
                sum += x % 10;
                x /= 10;
            }
            if (sum > 0) count += 1;
        }
        return count;
    }
}

