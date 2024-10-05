        String binaryString = Integer.toBinaryString(N);
        int sum = 0;

        for (char c : binaryString.toCharArray()) {
            sum += Character.getNumericValue(c);
        }

        return Integer.toBinaryString(sum);
     }
}

