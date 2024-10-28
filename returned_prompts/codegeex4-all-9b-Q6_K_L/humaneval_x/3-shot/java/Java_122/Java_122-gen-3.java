        int sum = 0;
        for (int i = 0; i < k; i++) {
            int current = arr.get(i);
            if (current < 10) {
                sum += current;
            } else if (current < 100) {
                sum += current % 10;
            }
        }
        return sum;
    }
}

