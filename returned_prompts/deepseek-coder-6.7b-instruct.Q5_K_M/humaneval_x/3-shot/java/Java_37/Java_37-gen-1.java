        List<Integer> evenIndices = new ArrayList<>();
        for (int i = 0; i < l.size(); i += 2) {
            evenIndices.add(l.get(i));
        }
        Collections.sort(evenIndices);

        for (int i = 0, j = 0; i < l.size(); i += 2, ++j) {
            l.set(i, evenIndices.get(j));
        }
        return l;
     }
}

