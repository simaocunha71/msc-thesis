        int sum = 0;
        for (Object obj : lst) {
            if (obj instanceof Integer && (int)obj % 2 == 1 && (int)obj > 0) {
                sum += Math.pow((int)obj, 2);
            }
        }
        return sum;
    }
}

