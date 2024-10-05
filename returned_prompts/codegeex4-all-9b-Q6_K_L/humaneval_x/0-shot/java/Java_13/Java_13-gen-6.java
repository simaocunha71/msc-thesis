public int greatestCommonDivisor(int a, int b) {
        int max = Math.max(a, b);
        int min = Math.min(a, b);
        if (max % min == 0) {
            return min;
        } else {
            return greatestCommonDivisor(min, max % min);
        }
    }