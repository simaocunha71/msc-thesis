        if (a + b <= c || b + c <= a || c + a <= b) return -1;
        double p = (a + b + c) / 2;
        return Math.sqrt(p * (p - a) * (p - b) * (p - c));
    }
}

