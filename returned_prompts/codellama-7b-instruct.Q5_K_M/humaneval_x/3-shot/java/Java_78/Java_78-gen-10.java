        int result = 0;

        for (int i = 0; i < num.length(); i++) {
            int digit = Character.getNumericValue(num.charAt(i));
            if (digit == 1 || digit == 3 || digit == 5 || digit == 7 || digit == 11 || digit == 13) {
                result += 1;
            }
        }
        return result;
    }
}

