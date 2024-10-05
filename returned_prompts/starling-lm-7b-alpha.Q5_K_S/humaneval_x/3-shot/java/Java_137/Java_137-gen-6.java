        if (a instanceof Integer && b instanceof Integer) {
            if (a.equals(b)) return Optional.empty();
            return Optional.of(((Integer) a) > ((Integer) b) ? a : b);
        } else if (a instanceof Float && b instanceof Float) {
            if (a.equals(b)) return Optional.empty();
            return Optional.of(((Float) a) > ((Float) b) ? a : b);
        } else if (a instanceof Double && b instanceof Double) {
            if (a.equals(b)) return Optional.empty();
            return Optional.of(((Double) a) > ((Double) b) ? a : b);
        } else if (a instanceof String && b instanceof String) {
            if (a.equals(b)) return Optional.empty();
            if (a.toString().contains(".") && b.toString().contains(".")) {
                String[] a_split = ((String) a).split("[.,]");
                String[] b_split = ((String) b).split("[.,]");
                if (a_split.length == 1 && b_split.length == 1) {
                    return Optional.of(((String) a) > ((String) b) ? a : b);
                }
                if (a_split.length == 2 && b_split.length == 2) {
                    if (a_split[1].length() == 1 && b_split[1].length() == 1) {
                        if (a_split[0].equals(b_split[0])) {
                            return Optional.of(((String) a) > ((String) b) ? a : b);
                        } else {
                            return Optional.of(((String) a) > ((String) b) ? b : a);
                        }
                    } else {
                        return Optional.of(((String) a) > ((String) b) ? a : b);
                    }
                } else {
                    return Optional.of(((String) a) > ((String) b) ? a : b);
                }
            } else {
                return Optional.of(((String) a) > ((String) b)