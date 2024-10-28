        if (n > m) {
            return -1;
        } else {
            double avg = (n + m) / 2.0;
            int avg_int = (int) Math.round(avg);
            String avg_binary = Integer.toBinaryString(avg_int);
            return avg_binary;
        }
    }
}

