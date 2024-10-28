        List<Integer> result = new ArrayList<>();
        List<Integer> l1_copy = new ArrayList<>(l1);

        for (int i = 0; i < l1_copy.size(); i++) {
            if (l2.contains(l1_copy.get(i))) {
                result.add(l1_copy.get(i));
                l1_copy.set(i, Integer.MAX_VALUE);
            }
        }
        return result;
    }
}

