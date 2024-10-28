        int result = 0;
        for (Object o : lst) {
            if (o instanceof Integer) {
                int n = (Integer) o;
                if (n > 0 && n % 2 == 1) {
                    result += n * n;
                }
            }
        }
        return result;
    }
}

