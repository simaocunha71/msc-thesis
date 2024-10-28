        int result = 0;
        for (Object x : lst) {
            if (x instanceof Integer && (Integer) x >= 0) {
                result += Math.pow((Integer) x, 2);
            }
        }
        return result;
    }
}

