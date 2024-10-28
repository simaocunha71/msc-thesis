        int count = 0;
        while (N > 0) {
            int reminder = N % 2;
            count += reminder;
            N /= 2;
        }
        String binary = Integer.toBinaryString(count);
        return binary;
    }
}
