        List<Integer> result = new ArrayList<>();
        for (int i : x) {
            if (i % 2 != 0) {
                result.add(i);
            }
        }
        result.sort(Comparator.naturalOrder());
        return result;
    }
}

