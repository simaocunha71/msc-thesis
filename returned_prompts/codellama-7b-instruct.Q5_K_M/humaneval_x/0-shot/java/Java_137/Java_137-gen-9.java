        if (a instanceof Integer) {
            if (b instanceof Integer) {
                if (((Integer) a) > ((Integer) b)) {
                    return Optional.of(a);
                } else if (((Integer) a) < ((Integer) b)) {
                    return Optional.of(b);
                } else {
                    return Optional.empty();
                }
            } else if (b instanceof Double) {
                if (((Integer) a) > ((Double) b).intValue()) {
                    return Optional.of(a);
                } else if (((Integer) a) < ((Double) b).intValue()) {
                    return Optional.of(b);
                } else {
                    return Optional.empty();
                }
            } else if (b instanceof String) {
                String strB = b.toString();
                if (strB.contains(".")) {
                    if (((Integer) a) > Double.parseDouble(strB)) {
                        return Optional.of(a);
                    } else if (((Integer) a) < Double.parseDouble(strB)) {
                        return Optional.of(b);
                    } else {
                        return Optional.empty();
                    }
                } else {
                    int intB = Integer.parseInt(b.toString());
                    if (((Integer) a) > intB) {
                        return Optional.of(a);
                    } else if (((Integer) a) < intB) {
                        return Optional.of(b);
                    } else {
                        return Optional.empty();
                    }
                }
            }
        } else if (a instanceof Double) {
            if (b instanceof Integer) {
                if (((Double) a).intValue() > ((Integer) b)) {
                    return Optional.of(a);
                } else if (((Double) a).intValue() < ((Integer) b)) {
                    return Optional.of(b);
                } else {
                    return Optional.empty();
                }
            } else if (b instanceof Double) {
                if (((Double) a) > ((Double) b)) {
                    return Optional.