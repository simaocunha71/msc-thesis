        if (a instanceof Integer && b instanceof Integer) {
            if ((int) a > (int) b) return Optional.of(a);
            else if ((int) a < (int) b) return Optional.of(b);
            else return Optional.empty();
        } else if (a instanceof Double && b instanceof Double) {
            if ((double) a > (double) b) return Optional.of(a);
            else if ((double) a < (double) b) return Optional.of(b);
            else return Optional.empty();
        } else if (a instanceof String && b instanceof String) {
            if (compareString(a.toString(), b.toString()) > 0) return Optional.of(a);
            else if (compareString(a.toString(), b.toString()) < 0) return Optional.of(b);
            else return Optional.empty();
        } else {
            throw new RuntimeException("Invalid inputs");
        }
    }

    private int compareString(String a, String b) {
        String[] partsA = a.replace(",", ".").split("\\.");
        String[] partsB = b.replace(",", ".").split("\\.");
        int i = 0;
        while (i < partsA.length && i < partsB.length) {
            if (Double.parseDouble(partsA[i]) > Double.parseDouble(partsB[i])) {
                return 1;
            } else if (Double.parseDouble(partsA[i]) < Double.parseDouble(partsB[i])) {
                return -1;
            }
            i++;
        }
        if (i == partsA.length) {
            if (partsB.length > i) {
                return -1;
            }
        } else {
            if (partsA.length > i) {
                return 1;
            }
        }
        return 0;
    }
}

