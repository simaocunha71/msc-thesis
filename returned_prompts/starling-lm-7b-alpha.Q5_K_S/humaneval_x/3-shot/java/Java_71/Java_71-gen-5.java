        if (a + b <= c || c + b <= a || a + c <= b) {
            return -1;
        }
        double s = (a + b + c) / 2;
        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }
}


