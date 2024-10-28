        int sum = 0;
        String binary = Integer.toBinaryString(N);
        for (char c : binary.toCharArray()) {
            sum += c - '0';
        }
        return Integer.toBinaryString(sum);
    }
}

