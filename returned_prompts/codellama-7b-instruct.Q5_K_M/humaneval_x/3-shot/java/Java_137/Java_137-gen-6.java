        if (a.getClass() != b.getClass()) throw new IllegalArgumentException("Arguments must be of the same type");
        if (a instanceof Double || a instanceof Float) {
            if (a.equals(b)) return Optional.empty();
            if ((double) a > (double) b) return Optional.of(a);
            else return Optional.of(b);
        } else if (a instanceof String) {
            String sa = (String) a;
            String sb = (String) b;
            if (sa.equals(sb)) return Optional.empty();
            if (sa.length() < sb.length()) return Optional.of(sb);
            else return Optional.of(sa);
        } else {
            if (a.equals(b)) return Optional.empty();
            if ((int) a > (int) b) return Optional.of(a);
            else return Optional.of(b);
        }
    }
}

