        if (a + b > c && a + c > b && b + c > a) {
            double s = (a + b + c) / 2.0;
            return Math.sqrt(s * (s - a) * (s - b) * (s - c));
        }
        return -1.0;
    }
}

