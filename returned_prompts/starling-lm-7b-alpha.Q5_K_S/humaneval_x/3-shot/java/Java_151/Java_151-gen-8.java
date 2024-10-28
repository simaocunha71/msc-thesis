        int result = 0;
        for (Object o : lst) {
            if (o instanceof Integer) {
                Integer n = (Integer) o;
                if (n % 2 == 1) {
                    result += n * n;
                }
            }
        }
        return result;
    }
}


