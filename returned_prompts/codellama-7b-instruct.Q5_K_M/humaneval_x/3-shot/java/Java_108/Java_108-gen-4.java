        int count = 0;
        for (Integer x : arr) {
            int sum = 0;
            while (x != 0) {
                sum += x % 10;
                x /= 10;
            }
            if (sum > 0) count++;
        }
        return count;
    }
}

