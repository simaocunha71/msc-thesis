        int integerPart = (int) Math.floor(Math.abs(Double.parseDouble(value)));
        double decimalPart = Math.abs(Double.parseDouble(value)) - integerPart;
        if (decimalPart >= 0.5) {
            return integerPart + 1;
        } else {
            return integerPart;
        }
    }
}

