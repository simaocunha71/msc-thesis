        if (a == 0) {
            return b;
        }
        if (b == 0) {
            return a;
        }
        if (a < b) {
            return greatestCommonDivisor(b, a);
        }
        int r = a % b;
        if (r == 0) {
            return b;
        }
        return greatestCommonDivisor(b, r);
    }
}


