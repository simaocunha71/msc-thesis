        double num = Double.parseDouble(value);
        int intPart = (int) num;
        double fracPart = num - intPart;

        if (fracPart < 0.5) {
            return intPart;
        } else if (fracPart > 0.5) {
            if (intPart > 0) {
                return intPart + 1;
            } else {
                return intPart - 1;
            }
        } else {
            if (intPart > 0) {
                return intPart + 1;
            } else {
                return intPart - 1;
            }
        }
    }
}

