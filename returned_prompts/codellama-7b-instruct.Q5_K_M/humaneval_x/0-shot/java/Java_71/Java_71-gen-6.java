        double s = a + b + c;
        if (s <= a || s <= b || s <= c) return -1;
        double p = (s - a) * (s - b) * (s - c);
        return Math.sqrt(p);
    }
}
