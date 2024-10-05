        if (a.equals(b)) {
            return Optional.empty();
        }
        if (a instanceof Integer && b instanceof Integer) {
            return Optional.of(((Integer) a) > ((Integer) b) ? a : b);
        }
        if (a instanceof Double && b instanceof Double) {
            return Optional.of(((Double) a) > ((Double) b) ? a : b);
        }
        if (a instanceof Float && b instanceof Float) {
            return Optional.of(((Float) a) > ((Float) b) ? a : b);
        }
        if (a instanceof String && b instanceof String) {
            String[] aParts = ((String) a).split(",");
            String[] bParts = ((String) b).split(",");
            int aPartsLength = aParts.length;
            int bPartsLength = bParts.length;
            int aFirstPart = Integer.parseInt(aParts[0]);
            int bFirstPart = Integer.parseInt(bParts[0]);
            if (aFirstPart == bFirstPart) {
                int aSecondPart = aPartsLength == 1 ? 0 : Integer.parseInt(aParts[1]);
                int bSecondPart = bPartsLength == 1 ? 0 : Integer.parseInt(bParts[1]);
                if (aSecondPart == bSecondPart) {
                    return Optional.empty();
                }
                return Optional.of(aSecondPart > bSecondPart ? a : b);
            }
            return Optional.of(aFirstPart > bFirstPart ? a : b);
        }
        return Optional.of(a);
    }
}
