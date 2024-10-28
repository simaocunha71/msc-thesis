        double num = Double.parseDouble(value);
        int integerPart = (int) num;
        if (num - integerPart > 0.5) {
            return integerPart + 1;
        } else if (num - integerPart < -0.5) {
            return integerPart - 1;
        } else {
            return integerPart;
        }
    }
}

