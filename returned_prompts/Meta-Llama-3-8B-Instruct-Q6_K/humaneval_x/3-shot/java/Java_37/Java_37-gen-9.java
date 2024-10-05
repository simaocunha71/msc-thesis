        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                result.add Collections.sort(Arrays.asList(l.get(i), l.get(i + 1))).get(0);
            } else {
                result.add l.get(i);
            }
        }
        return result;
    }
}

