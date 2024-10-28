        if (a + b > c && b + c > a && c + a > b) {
            double s = (a + b + c) / 2;
            double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
            return String.format("%.2f", area);
        } else {
            return -1;
        }
    }
}

