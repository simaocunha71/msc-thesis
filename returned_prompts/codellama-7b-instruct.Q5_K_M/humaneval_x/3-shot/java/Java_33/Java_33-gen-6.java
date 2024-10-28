        List<Integer> l1 = new ArrayList<>(l);
        List<Integer> l2 = new ArrayList<>(l);
        Collections.sort(l2);
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < l1.size(); i++) {
            if (i % 3 == 0) {
                result.add(l2.get(i % l2.size()));
            } else {
                result.add(l1.get(i));
            }
        }
        return result;
    }
}

