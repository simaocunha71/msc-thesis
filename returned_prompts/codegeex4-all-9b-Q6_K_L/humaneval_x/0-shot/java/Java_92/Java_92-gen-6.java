public boolean anyInt(Object x, Object y, Object z) {
        // Check if all three inputs are integers
        if (!(x instanceof Integer) || !(y instanceof Integer) || !(z instanceof Integer)) {
            return false;
        }

        // Check if any number is the sum of the other two
        int sum = (Integer) x + (Integer) y + (Integer) z;
        if (sum - (Integer) x == (Integer) y && sum - (Integer) x == (Integer) z) {
            return true;
        }
        if (sum - (Integer) y == (Integer) x && sum - (Integer) y == (Integer) z) {
            return true;
        }
        if (sum - (Integer) z == (Integer) x && sum - (Integer) z == (Integer) y) {
            return true;
        }

        return false;
    }