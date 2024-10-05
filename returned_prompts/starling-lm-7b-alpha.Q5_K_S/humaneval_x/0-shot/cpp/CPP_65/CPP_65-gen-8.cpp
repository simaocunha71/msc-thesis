        if (a == 0) return b;
        if (b == 0) return a;
        if (a > b) return greatestCommonDivisor(a % b, b);
        return greatestCommonDivisor(a, b % a);
    }
}

