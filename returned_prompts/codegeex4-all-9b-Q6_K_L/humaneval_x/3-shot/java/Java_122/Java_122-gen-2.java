        int sum = 0;
        for (int i = 0; i < k; i++) {
            int num = arr.get(i);
            if (num < 10) {
                sum += num;
            } else {
                sum += num % 10;
            }
        }
        return sum;
    }
}

