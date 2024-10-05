        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                result.add(l.get(i));
            } else if (i % 3 == 1) {
                result.add(l.get(i));
            } else if (i % 3 == 2) {
                result.add(l.get(i));
            }
        }
        result.sort(Integer::compare);
        return result;
    }
}
