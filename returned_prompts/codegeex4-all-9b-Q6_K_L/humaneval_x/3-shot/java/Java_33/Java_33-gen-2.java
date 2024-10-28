        List<Integer> result = new ArrayList<>();
        List<Integer> sorted = new ArrayList<>();

        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) sorted.add(l.get(i));
        }
        Collections.sort(sorted);

        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) result.add(sorted.remove(0));
            else result.add(l.get(i));
        }
        return result;
    }
}

