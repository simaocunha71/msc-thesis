        int sum = 0;
        for (Object o : lst) {
            try {
                int i = (int) o;
                if (i % 2 != 0) {
                    sum += i * i;
                }
            } catch (Exception e) {
            }
        }
        return sum;
    }
}

