        if (a + b > c && a + c > b && b + c > a) {
            return Math.sqrt((a + b + c) * ((a + b + c) - a) * ((a + b + c) - b) * ((a + b + c) - c)) / 4.0;
        }
        return -1;
    }
}

