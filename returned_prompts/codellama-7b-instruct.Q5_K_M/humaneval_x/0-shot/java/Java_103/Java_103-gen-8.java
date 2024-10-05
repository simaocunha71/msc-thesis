        if (n > m) {
            return -1;
        }
        double average = (n + m) / 2.0;
        int roundedAverage = (int) Math.round(average);
        String binary = Integer.toBinaryString(roundedAverage);
        return binary;
    }
}
