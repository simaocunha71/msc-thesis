        int decimalPart = (int) (Double.parseDouble(value) % 1.0 * 10);
        if (decimalPart >= 5) {
            return (int) Math.ceil(Double.parseDouble(value));
        } else {
            return (int) Math.floor(Double.parseDouble(value));
        }
    }
}

