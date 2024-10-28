        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                result.add(sort(l.subList(i, i + 1)).get(0));
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }

    private List<Integer> sort(List<Integer> l) {
        Collections.sort(l);
        return l;
    }
}

