        if (x < base) return Integer.toString(x);
        int quotient = x / base;
        int remainder = x % base;
        return changeBase(quotient, base) + Integer.toString(remainder);
    }
}

