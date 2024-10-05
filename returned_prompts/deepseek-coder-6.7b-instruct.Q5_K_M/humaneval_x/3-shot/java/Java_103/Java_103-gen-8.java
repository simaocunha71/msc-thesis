        if (n > m) {
            return -1;
        }

        int avg = (n + m) / 2;
        avg = (int) Math.ceil(avg);

        return Integer.toBinaryString(avg);
    }
}

