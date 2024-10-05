        if (a instanceof String && b instanceof String) {
            String[] a_parts = ((String) a).split("[.,]");
            String[] b_parts = ((String) b).split("[.,]");
            if (a_parts.length == 1 && b_parts.length == 1) {
                if (a_parts[0].equals(b_parts[0])) {
                    return Optional.empty();
                } else if (a_parts[0].compareTo(b_parts[0]) > 0) {
                    return Optional.of(a);
                } else {
                    return Optional.of(b);
                }
            } else if (a_parts.length == 1 && b_parts.length == 2) {
                if (a_parts[0].equals(b_parts[0])) {
                    return Optional.empty();
                } else if (a_parts[0].compareTo(b_parts[0]) > 0) {
                    return Optional.of(a);
                } else {
                    return Optional.of(b);
                }
            } else if (a_parts.length == 2 && b_parts.length == 1) {
                if (a_parts[0].equals(b_parts[0])) {
                    return Optional.empty();
                } else if (a_parts[0].compareTo(b_parts[0]) < 0) {
                    return Optional.of(a);
                } else {
                    return Optional.of(b);
                }
            } else if (a_parts.length == 2 && b_parts.length == 2) {
                if (a_parts[0].equals(b_parts[0]) && a_parts[1].equals(b_parts[1])) {
                    return Optional.empty();
                } else if (a_parts[0].compareTo(b_parts[0]) < 0 && a_parts[1].compareTo(b_parts[1]) > 0) {
                    return Optional.of(a);
                } else if (a_parts[0