        int sum = 0;
        for (Object o : lst) {
            if (o instanceof Integer && (Integer) o > 0) {
                sum += (int) Math.pow((Integer) o, 2);
            }
        }
        return sum;
    }
}

