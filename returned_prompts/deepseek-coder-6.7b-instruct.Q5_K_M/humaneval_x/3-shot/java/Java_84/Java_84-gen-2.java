        String binary = Integer.toBinaryString(N);
        int sum = 0;
        for (char c : binary.toCharArray()) {
            sum += Character.getNumericValue(c);
        }
        return Integer.toBinaryString(sum);
    }
}

