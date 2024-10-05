        int sum = 0;
        for (Object o : lst) {
            if (!(o instanceof Number)) continue A;
            Number n = (Number) o;
            if (n.doubleValue() < 0) continue A;
            sum += n.intValue() * n.intValue();
        }
        return sum;
    }
}
