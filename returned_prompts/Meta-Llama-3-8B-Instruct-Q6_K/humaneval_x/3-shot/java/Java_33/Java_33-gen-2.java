        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                List<Integer> sorted = new ArrayList<>();
                for (int j = i; j < l.size(); j += 3) {
                    sorted.add(l.get(j));
                }
                Collections.sort(sorted);
                result.add(sorted.get(0));
                i += 2;
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
}

