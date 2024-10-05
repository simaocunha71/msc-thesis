        if (n > m) {
            return -1;
        } else {
            double avg = (n + m) / 2.0;
            return Integer.toBinaryString((int) Math.round(avg));
        }
    }
}

