        if (a + b <= c || b + c <= a || a + c <= b) {
            return -1;
        }
        double area = (a + b + c) / 2;
        double s = Math.sqrt(area * (area - a) * (area - b) * (area - c));
        return s;
    }
}
