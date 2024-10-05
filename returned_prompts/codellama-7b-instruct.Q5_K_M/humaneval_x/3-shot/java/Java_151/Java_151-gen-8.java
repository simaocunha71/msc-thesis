        int sum = 0;
        for (Object x : lst) {
            if (x instanceof Double) {
                double d = (double) x;
                if (d >= 0 && d == (int) d) {
                    sum += (int) d * (int) d;
                }
            }
        }
        return sum;
    }
}

