        if (x < base) return String.valueOf(x);
        else {
            int remainder = x % base;
            int quotient = x / base;
            return changeBase(quotient, base) + String.valueOf(remainder);
        }
    }
}

