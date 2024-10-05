        double number = Double.parseDouble(value);
        int integerPart = (int) Math.floor(number);
        double fractionalPart = number - integerPart;

        if (fractionalPart >= 0.5) {
            return integerPart + 1;
        } else {
            return integerPart;
        }
    }
}

