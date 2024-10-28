        double a_num = getNum(a);
        double b_num = getNum(b);

        if (a_num == b_num) return Optional.empty();
        else if (a_num > b_num) return Optional.of(a);
        else return Optional.of(b);
    }

    private double getNum(Object a) {
        if (a instanceof String) {
            String a_str = (String) a;
            String a_num_str = a_str.replace(",", ".");
            return Double.parseDouble(a_num_str);
        } else if (a instanceof Double) {
            return (Double) a;
        } else if (a instanceof Float) {
            return (Float) a;
        } else if (a instanceof Integer) {
            return (Integer) a;
        } else {
            throw new IllegalArgumentException("Invalid type");
        }
    }
}

