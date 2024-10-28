        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                List<Integer> temp = new ArrayList<>(Arrays.asList(l.get(i)));
                Collections.sort(temp);
                result.addAll(temp);
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
}