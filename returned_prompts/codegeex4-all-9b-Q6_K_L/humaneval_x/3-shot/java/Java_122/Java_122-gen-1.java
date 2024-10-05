        int sum = 0;
        for (int i = 0; i < k; i++) {
            int current = arr.get(i);
            while (current >= 10) current /= 10;

            sum += current;
        }
        return sum;
    }
}

