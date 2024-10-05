        String binary = Integer.toBinaryString(N);
        int sum = 0;
        for (int i = 0; i < binary.length(); i++) {
            sum += binary.charAt(i) - '0';
        }
        return Integer.toBinaryString(sum);
    }
}