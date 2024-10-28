        if (a instanceof String && b instanceof String) {
            String sa = (String) a;
            String sb = (String) b;
            if (sa.contains(",") && sb.contains(",")) {
                return Optional.of(sb);
            } else if (sa.contains(",") && !sb.contains(",")) {
                return Optional.of(sa);
            } else if (!sa.contains(",") && sb.contains(",")) {
                return Optional.of(sb);
            } else {
                return Optional.of(a);
            }
        }

        if (a instanceof String || b instanceof String) {
            String sa = a.toString();
            String sb = b.toString();
            if (sa.contains(",") && sb.contains(",")) {
                return Optional.of(sb);
            } else if (sa.contains(",") && !sb.contains(",")) {
                return Optional.of(sa);
            } else if (!sa.contains(",") && sb.contains(",")) {
                return Optional.of(sb);
            } else {
                return Optional.of(a);
            }
        }

        if (a instanceof Double && b instanceof Double) {
            double da = (double) a;
            double db = (double) b;
            if (da == db) {
                return Optional.empty();
            } else {
                return Optional.of((da > db) ? a : b);
            }
        }

        if (a instanceof Float && b instanceof Float) {
            float fa = (float) a;
            float fb = (float) b;
            if (fa == fb) {
                return Optional.empty();
            } else {
                return Optional.of((fa > fb) ? a : b);
            }
        }

        if (a instanceof Integer && b instanceof Integer) {
            int ia = (int) a;
            int ib = (int) b;
            if (ia == ib) {
                return Optional.empty();
            } else {
                return Optional.of((ia > ib) ? a : b);
            }
        }

        return