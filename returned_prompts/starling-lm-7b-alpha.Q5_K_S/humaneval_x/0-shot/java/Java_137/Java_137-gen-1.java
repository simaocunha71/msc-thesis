    if (a instanceof Integer && b instanceof Integer) {
        if ((int) a == (int) b) {
            return Optional.empty();
        }
        return Optional.of((int) Math.max(a, b));
    } else if (a instanceof Float && b instanceof Float) {
        if ((float) a == (float) b) {
            return Optional.empty();
        }
        return Optional.of((float) Math.max(a, b));

    } else if (a instanceof String && b instanceof String) {
        if (a.toString().equals(b.toString())) {
            return Optional.empty();
        }
        if (a.toString().contains(".") && b.toString().contains(".")) {
            if (a.toString().split("\\.")[1].length() < b.toString().split("\\.")[1].length()) {
                return Optional.of(b);
            }
            return Optional.of(a);
        }
        if (a.toString().contains(",") && b.toString().contains(",")) {
            if (a.toString().split(",")[1].length() < b.toString().split(",")[1].length()) {
                return Optional.of(b);
            }
            return Optional.of(a);
        }
        if (a.toString().contains(".") && !b.toString().contains(".")) {
            return Optional.of(a);
        }
        if (!a.toString().contains(".") && b.toString().contains(".")) {
            return Optional.of(b);
        }
        if (!a.toString().contains(".") && !b.toString().contains(".")) {
            return Optional.of(a);
        }
        if (a.toString().split(",")[1].length() < b.toString().split(",")[1].length()) {
            return Optional.of(b);
        }
        return Optional.of(a);
    } else {
        return Optional.empty();
    }

    }
}

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.compareOne(1,