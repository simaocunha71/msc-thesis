        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                int sorted = 0;
                for (int j = i; j < l.size(); j += 3) {
                    sorted = Math.min(sorted, l.get(j));
                }
                result.add(sorted);
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
}

