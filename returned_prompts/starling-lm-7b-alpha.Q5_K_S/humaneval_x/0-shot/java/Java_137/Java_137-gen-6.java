    double d1, d2;
    if (a instanceof Integer || a instanceof Float || a instanceof Double) {
        d1 = (double)a;
    } else if (a instanceof String) {
        d1 = Double.parseDouble(String.valueOf(a));
    } else {
        return Optional.empty();
    }
    if (b instanceof Integer || b instanceof Float || b instanceof Double) {
        d2 = (double)b;
    } else if (b instanceof String) {
        d2 = Double.parseDouble(String.valueOf(b));
    } else {
        return Optional.empty();
    }
    if (d1 == d2) {
        return Optional.empty();
    } else if (d1 > d2) {
        return Optional.of(d1);
    } else {
        return Optional.of(d2);
    }
}

    /**
    Create a function that takes three integer values and returns true if all
    three values are the same, and false if the values are not the same.
    Note: If the three input values are equal, the function should return true.

    areEqual(1, 1, 1) -> true
    areEqual(1, 2, 3) -> false
    areEqual(3, 3, 1) -> true
     */
    public boolean areEqual(int a, int b, int c) {
        if (a == b && a == c) {
            return true;
        } else {
            return false;
        }
    }

    /**
    Create a function that takes an array of integers and returns an array of
    integers where all the values are the same. The length of the returned array
    should be equal to the length of the input array. The values of the array are
    chosen from the input array, but the order of the values does not matter.
    Note: The function should return an array of the same length as the input array,
    but the order of the values does not matter.

    makeEqual(1, 1, 2) -> [1, 1, 2]
    makeEqual(1, 2, 3) -> [1, 2