        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                result.add(l.get(i));
            }
        }
        Collections.sort(result);
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 1) {
                result.add(l.get(i));
            }
        }
        return result;

    }
}

