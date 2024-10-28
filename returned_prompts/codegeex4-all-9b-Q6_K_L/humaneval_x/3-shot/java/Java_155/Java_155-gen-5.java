        int evenCount = 0;
        int oddCount = 0;

        for (char c : String.valueOf(Math.abs(num)).toCharArray()) {
            if (Character.getNumericValue(c) % 2 == 0) evenCount += 1;
            else oddCount += 1;
        }
        return Arrays.asList(evenCount, oddCount);
    }
}

