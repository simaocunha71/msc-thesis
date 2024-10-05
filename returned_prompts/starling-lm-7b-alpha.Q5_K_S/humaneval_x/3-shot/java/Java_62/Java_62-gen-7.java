        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < xs.size(); i++) {
            if (i + 1 < xs.size()) {
                result.add(i + 1, xs.get(i + 1));
            } else {
                result.add(i + 1);
            }
        }
        result.set(0, xs.get(0) * 2);
        for (int i = 1; i < result.size(); i++) {
            result.set(i, result.get(i - 1) + result.get(i));
        }
        result.subList(0, result.size() - 1).clear();
        return result;
    }
}

