        int sum = 0;
        for (Object obj : lst) {
            if (obj instanceof Integer && ((Integer) obj) > 0) {
                sum += Math.pow((Integer) obj, 2);
            }
        }
        return sum;
    }
}

