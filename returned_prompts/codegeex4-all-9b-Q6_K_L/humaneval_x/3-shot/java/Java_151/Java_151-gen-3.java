        int sum = 0;
        for (Object o : lst) {
            if (o instanceof Integer) {
                int i = (Integer) o;
                if (i > 0 && i % 2 == 1) {
                    sum += i * i;
                }
            }
        }
        return sum;
    }
}

