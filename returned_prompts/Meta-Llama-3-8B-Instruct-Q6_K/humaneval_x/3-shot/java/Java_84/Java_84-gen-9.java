        int sum = 0;
        String binary = Integer.toBinaryString(N);
        for (int i = 0; i < binary.length(); i++) {
            sum += binary.charAt(i) - '0';
        }
        return Integer.toBinaryString(sum);
    }
}

