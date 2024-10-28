        int result = 1;
        for (char c : Integer.toString(n).toCharArray()) {
            int digit = Character.getNumericValue(c);
            if (digit % 2 != 0) result *= digit;
        }
        return result;
    }
}

