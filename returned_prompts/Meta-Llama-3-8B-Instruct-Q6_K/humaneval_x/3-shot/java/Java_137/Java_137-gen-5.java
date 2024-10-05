        if (a instanceof Integer && b instanceof Integer) {
            if (((Integer) a).compareTo((Integer) b) > 0) {
                return Optional.of(a);
            } else if (((Integer) a).compareTo((Integer) b) < 0) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Float && b instanceof Float) {
            if (((Float) a).compareTo((Float) b) > 0) {
                return Optional.of(a);
            } else if (((Float) a).compareTo((Float) b) < 0) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof String && b instanceof String) {
            String str1 = (String) a;
            String str2 = (String) b;
            str1 = str1.replace(",", ".");
            str2 = str2.replace(",", ".");
            if (Double.parseDouble(str1) > Double.parseDouble(str2)) {
                return Optional.of(a);
            } else if (Double.parseDouble(str1) < Double.parseDouble(str2)) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Integer && b instanceof Float) {
            if (((Integer) a) > ((Float) b)) {
                return Optional.of(a);
            } else if (((Integer) a) < ((Float) b)) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Float && b instanceof Integer) {
            if (((Float) a) > ((Integer) b)) {
                return Optional.of(a);
            } else if (((Float) a) < ((Integer) b)) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof String && b instanceof Float) {
            if (Double.parseDouble(((String) a).replace(",", ".")) > ((Float) b)) {
                return Optional.of(a);
            } else if (Double.parseDouble(((String) a).replace(",", ".")) < ((Float) b)) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Float && b instanceof String) {
            if (((Float) a) > Double.parseDouble(((String) b).replace(",", "."))) {
                return Optional.of(a);
            }