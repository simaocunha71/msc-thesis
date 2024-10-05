        int sum = 0;
        String binary = Integer.toBinaryString(N);
        for (char c : binary.toCharArray()) {
            if (c == '1') {
                sum += 1;
            }
        }
        return String.valueOf(sum);
    }
}

