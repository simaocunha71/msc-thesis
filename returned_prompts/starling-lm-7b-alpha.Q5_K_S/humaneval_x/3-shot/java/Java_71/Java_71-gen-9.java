        if (a + b <= c || a + c <= b || b + c <= a) {
            return -1.0;
        }
        double s = 0.5 * (a + b + c);
        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }
}

