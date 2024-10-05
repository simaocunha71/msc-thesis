        int evenCount = 0;
        int oddCount = 0;

        String str = String.valueOf(num);
        for (char c : str.toCharArray()) {
            int digit = Character.getNumericValue(c);
            if (digit % 2 == 0) {
                evenCount += 1;
            } else {
                oddCount += 1;
            }
        }
        return Arrays.asList(evenCount, oddCount);
    }
}

