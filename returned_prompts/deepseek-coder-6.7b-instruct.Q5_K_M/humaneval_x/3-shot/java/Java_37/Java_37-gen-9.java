        List<Integer> evenIndices = new ArrayList<>();
        for (int i = 0; i < l.size(); i += 2) {
            evenIndices.add(l.get(i));
        }

        Collections.sort(evenIndices);

        List<Integer> result = new ArrayList<>();
        int j = 0;
        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                result.add(evenIndices.get(j++));
            } else {
                result.add(l.get(i));
            }
        }

        return result;
    }
}

