        if (a instanceof Integer && b instanceof Integer) {
            if ((Integer) a > (Integer) b) return Optional.of(a);
            else if ((Integer) a < (Integer) b) return Optional.of(b);
            else return Optional.empty();
        }

        if (a instanceof Double && b instanceof Double) {
            if ((Double) a > (Double) b) return Optional.of(a);
            else if ((Double) a < (Double) b) return Optional.of(b);
            else return Optional.empty();
        }

        if (a instanceof String && b instanceof String) {
            String a_str = a.toString();
            String b_str = b.toString();
            if (a_str.contains(".") && b_str.contains(".")) {
                String a_comma = a_str.replaceAll("\\.", "");
                String b_comma = b_str.replaceAll("\\.", "");
                if (Integer.parseInt(a_comma) > Integer.parseInt(b_comma)) return Optional.of(a);
                else if (Integer.parseInt(a_comma) < Integer.parseInt(b_comma)) return Optional.of(b);
                else return Optional.empty();
            }

            if (a_str.contains(",") && b_str.contains(",")) {
                String a_comma = a_str.replaceAll("\\,", "");
                String b_comma = b_str.replaceAll("\\,", "");
                if (Integer.parseInt(a_comma) > Integer.parseInt(b_comma)) return Optional.of(a);
                else if (Integer.parseInt(a_comma) < Integer.parseInt(b_comma)) return Optional.of(b);
                else return Optional.empty();
            }
        }

        if (a instanceof Float && b instanceof Float) {
            if ((Float) a > (Float) b) return Optional.of(a);
            else if ((Float) a < (Float) b) return Optional.of(b);
            else return Optional.empty();
        }

        if (a instanceof String && b instanceof Float