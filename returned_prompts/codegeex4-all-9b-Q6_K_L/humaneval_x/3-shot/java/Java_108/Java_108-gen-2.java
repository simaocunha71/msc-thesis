        int count = 0;
        for (int i : arr) {
            int sum = 0;
            int abs = Math.abs(i);
            while (abs > 0) {
                sum += abs % 10;
                abs /= 10;
            }
            if (sum > 0) count += 1;
        }
        return count;
    }
}

