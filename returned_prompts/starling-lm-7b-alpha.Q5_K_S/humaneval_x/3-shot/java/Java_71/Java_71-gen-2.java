        if (a + b <= c || a + c <= b || b + c <= a) return -1;
        double s = (a + b + c) / 2;
        double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
        return Math.round(area * 100.0) / 100.0;
    }
}

