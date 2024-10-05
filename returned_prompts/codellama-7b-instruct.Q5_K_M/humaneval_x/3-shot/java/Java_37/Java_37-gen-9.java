        List<Integer> result = new ArrayList<>();
        int len = l.size();
        for (int i = 0; i < len; i++) {
            if (i % 2 == 0) {
                result.add(l.get(i));
            } else {
                result.add(sortEvenHelper(l.subList(i, len)));
            }
        }
        return result;
    }

    private Integer sortEvenHelper(List<Integer> l) {
        int len = l.size();
        List<Integer> sorted = new ArrayList<>();
        sorted.addAll(l);
        Collections.sort(sorted);
        return sorted.get(len / 2);
    }
}

