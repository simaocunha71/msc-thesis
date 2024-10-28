        double num = Double.parseDouble(value);
        int intPart = (int)num;
        double decimalPart = num - intPart;

        if (decimalPart < 0.5 && decimalPart > -0.5) {
            return intPart;
        } else if (decimalPart < 0) {
            return intPart;
        } else {
            return intPart + 1;
        }
    }
}

