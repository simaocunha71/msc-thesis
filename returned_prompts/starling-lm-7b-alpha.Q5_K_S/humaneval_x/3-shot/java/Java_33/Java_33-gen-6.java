        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 != 0) {
                result.add(l.get(i));
            } else {
                result.add(sortedValue(l.get(i)));
            }
        }
        return result;
    }

    private int sortedValue(int v) {
        List<Integer> l = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            l.add(v);
        }
        Collections.sort(l);
        return l.get(0);
    }
}


