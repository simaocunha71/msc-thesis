        if (a + b < c || b + c < a || c + a < b) return -1.0;

        double s = (a + b + c) / 2.0;
        return Math.round(Math.sqrt(s * (s - a) * (s - b) * (s - c)) * 100.0) / 100.0;
    }
}

