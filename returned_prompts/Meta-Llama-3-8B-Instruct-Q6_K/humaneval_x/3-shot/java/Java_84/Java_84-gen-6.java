        String binary = Integer.toBinaryString(N);
        int sum = 0;
        for (char c : binary.toCharArray()) {
            if (c == '1') {
                sum += 1;
            }
        }
        return Integer.toBinaryString(sum);
    }
}

