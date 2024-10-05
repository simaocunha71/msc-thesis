        int sum = 0;
        for (Object o : lst) {
            if (o instanceof Integer && ((Integer) o) > 0) {
                sum += ((Integer) o) * ((Integer) o);
            }
        }
        return sum;
    }
}

