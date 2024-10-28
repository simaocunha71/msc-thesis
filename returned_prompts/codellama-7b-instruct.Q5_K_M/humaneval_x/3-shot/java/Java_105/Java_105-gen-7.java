        List<String> result = new ArrayList<>();

        if (arr.isEmpty()) return result;

        int[] digits = new int[9];

        for (int i : arr) {
            if (i >= 1 && i <= 9) {
                digits[i - 1] += 1;
            }
        }

        Arrays.sort(digits);
        Arrays.sort(digits, 5, digits.length);
        Arrays.sort(digits, 0, 5, Collections.reverseOrder());

        for (int i = 0; i < digits.length; i++) {
            if (digits[i] != 0) {
                result.add(getDigitName(digits[i]));
            }
        }
        return result;
    }

    private String getDigitName(int digit) {
        switch (digit) {
            case 1:
                return "One";
            case 2:
                return "Two";
            case 3:
                return "Three";
            case 4:
                return "Four";
            case 5:
                return "Five";
            case 6:
                return "Six";
            case 7:
                return "Seven";
            case 8:
                return "Eight";
            case 9:
                return "Nine";
        }
        return null;
    }
}

