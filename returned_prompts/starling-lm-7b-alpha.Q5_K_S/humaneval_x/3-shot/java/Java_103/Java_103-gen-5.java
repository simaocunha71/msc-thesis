        if (n > m) {
            return -1;
        } else {
            int avg = (n + m) / 2;
            return Integer.toBinaryString(Math.round(avg));
        }
    }
}

