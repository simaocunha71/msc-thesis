        int integer = Integer.parseInt(value);
        double double_value = Double.parseDouble(value);

        if (Math.abs(integer - double_value) <= 0.5) {
            return integer + (integer < 0 ? 1 : -1);
        } else if (integer < double_value) {
            return integer + 1;
        } else {
            return integer - 1;
        }
    }
}

