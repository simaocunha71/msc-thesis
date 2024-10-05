        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                result.add(l.get(i));
            }
        }
        result.sort(Integer::compare);
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 != 0) {
                result.add(l.get(i));
            }
        }
        return result;
    }
}

