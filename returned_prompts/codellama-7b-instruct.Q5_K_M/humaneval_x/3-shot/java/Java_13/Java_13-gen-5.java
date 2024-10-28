        if (a == 0 || b == 0) return 0;
        if (a < b) return greatestCommonDivisor(b, a);
        return a % b == 0 ? b : greatestCommonDivisor(b, a % b);
    }
}

