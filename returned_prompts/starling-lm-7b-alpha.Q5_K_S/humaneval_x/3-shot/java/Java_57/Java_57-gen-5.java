        boolean isIncreasing = true;
        boolean isDecreasing = true;
        for (int i = 1; i < l.size(); i++) {
            if (l.get(i) < l.get(i - 1)) isIncreasing = false;
            if (l.get(i) > l.get(i - 1)) isDecreasing = false;
        }
        return isIncreasing || isDecreasing;
    }
}

