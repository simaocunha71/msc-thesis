        int sum = 0;
        for (Object o : lst) {
            if (o instanceof Integer) {
                int n = (int) o;
                if (n % 2 == 1 && n > 0) {
                    sum += n * n;
                }
            }
        }
        return sum;
    }
}

