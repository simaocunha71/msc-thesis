        String binary = Integer.toBinaryString(N);
        int sum = 0;
        for (char c : binary.toCharArray()) {
            sum += (c - '0');
        }
        return Integer.toString(sum);
    }
}

