        int sum = 0;
        for (Object obj : lst) {
            if (obj instanceof Number) {
                Number n = (Number) obj;
                if (n.doubleValue() >= 0 && n.intValue() == n.doubleValue()) {
                    sum += n.doubleValue() * n.doubleValue();
                }
            }
        }
        return sum;
    }
}
