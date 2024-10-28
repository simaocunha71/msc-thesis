        List<Integer> thirdIndices = new ArrayList<>();

        for (int i = 0; i < l.size(); i++) {
            if ((i + 1) % 3 == 0) {
                thirdIndices.add(l.get(i));
            }
        }

        Collections.sort(thirdIndices);

        for (int i = 0; i < l.size(); i++) {
            if ((i + 1) % 3 == 0) {
                l.set(i, thirdIndices.get(i / 3));
            }
        }

        return l;
    }
}

