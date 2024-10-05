        Integer max = null;
        Integer min = null;

        for (Integer i : lst) {
            if (i < 0 && (max == null || i > max)) {
                max = i;
            } else if (i > 0 && (min == null || i < min)) {
                min = i;
            }
        }

        return Arrays.asList(Optional.ofNullable(max), Optional.ofNullable(min));
    }
}

