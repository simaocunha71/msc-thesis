    if (a instanceof Integer && b instanceof Integer) {
        return (Integer)a > (Integer)b ? Optional.of(a) : Optional.empty();

    } else if (a instanceof Float && b instanceof Float) {
        return (Float)a > (Float)b ? Optional.of(a) : Optional.empty();

    } else if (a instanceof String && b instanceof String) {
        return a.toString().replace(",", ".") .compareTo(b.toString().replace(",", ".")) > 0 ? Optional.of(a) : Optional.empty();

    } else if ((a instanceof Float || a instanceof String) && b instanceof Integer) {
        return ((Float)a > (Integer)b) || (a.toString().replace(",", ".").compareTo(String.valueOf((Integer)b)) > 0) ? Optional.of(a) : Optional.empty();

    } else if ((b instanceof Float || b instanceof String) && a instanceof Integer) {
        return ((Float)b > (Integer)a) || (b.toString().replace(",", ".").compareTo(String.valueOf((Integer)a)) > 0) ? Optional.of(b) : Optional.empty();

    } else if ((a instanceof Float || a instanceof String) && (b instanceof Float || b instanceof String)) {
        return a.toString().replace(",", ".").compareTo(b.toString().replace(",", ".")) > 0 ? Optional.of(a) : Optional.empty();
    }

    return Optional.empty();
}
}


A: Here is the corrected version of your code. I made a few changes:


*

*I added the else if statement for the case when both a and b are strings. In this case, I compared the strings after replacing the comma by a dot (as you mentioned in your problem).

*I added else if statements for the case when a is a string and b is an integer or a float. In this case, I compared the string value of the integer or float with the string value of a.

*I added else if statements for the case when b is a string and a is an integer or a float. In this case