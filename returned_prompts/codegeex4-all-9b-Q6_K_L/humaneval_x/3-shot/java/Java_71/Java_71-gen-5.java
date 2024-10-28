        if (a + b > c && a + c > b && b + c > a) {
            return (Math.sqrt((a + b + c) * (a + b - c) * (b + c - a) * (c + a - b))) / 4.0;
        } else {
            return -1;
        }
    }
}

