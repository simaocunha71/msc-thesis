        int value_as_int = Integer.valueOf(value);
        if (value_as_int % 2 == 0) {
            return value_as_int / 2;
        } else {
            return (value_as_int + 1) / 2;
        }
    }
}

