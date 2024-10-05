        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                result.add(l.get(i));
            } else {
                List<Integer> even = l.subList(i, l.size());
                Collections.sort(even);
                result.add(even.get(0));
            }
        }
        return result;
    }
}

