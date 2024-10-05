        if (lst.size() == 0) return 0;
        double sum = 0;
        for (Object obj : lst) {
            if (obj instanceof Integer) {
                int i = (Integer) obj;
                if (i >= 0) {
                    if (i % 2 == 1) sum += i * i;
                }
            }
        }
        return (int) sum;
    }
}

