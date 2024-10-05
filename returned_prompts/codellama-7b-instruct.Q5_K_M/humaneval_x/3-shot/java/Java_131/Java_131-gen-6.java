        int product = 1;
        for (char c : String.valueOf(n).toCharArray()) {
            int digit = Character.getNumericValue(c);
            if (digit % 2 != 0) product *= digit;
        }
        return product;
    }
}

