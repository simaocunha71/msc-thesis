        List<Integer> result = new ArrayList<>();
        int i = 0;
        int j = lst.size() - 1;
        boolean min = true;

        while (i <= j) {
            if (min) {
                result.add(Collections.min(lst.subList(i, j + 1)));
                i += 1;
            } else {
                result.add(Collections.max(lst.subList(i, j + 1)));
                j -= 1;
            }
            min = !min;
        }
        return result;
    }
}

