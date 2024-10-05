        if (a + b > c && b + c > a && a + c > b) {
            double s = (a + b + c) / 2;
            return Math.sqrt(s * (s - a) * (s - b) * (s - c));
        }
        return -1;
    }
}

