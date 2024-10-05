        if (a + b <= c || a + c <= b || b + c <= a) {
            return -1;
        }
        double s = (a + b + c) / 2;
        return Math.round(Math.sqrt(s * (s - a) * (s - b) * (s - c)) * 100.0) / 100.0;
    }
}

