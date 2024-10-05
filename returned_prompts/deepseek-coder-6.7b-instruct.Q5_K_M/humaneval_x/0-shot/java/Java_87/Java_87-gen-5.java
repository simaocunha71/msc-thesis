        List<List<Integer>> coordinates = new ArrayList<>();

        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    List<Integer> coordinate = new ArrayList<>();
                    coordinate.add(i);
                    coordinate.add(j);
                    coordinates.add(coordinate);
                }
            }
        }

        Collections.sort(coordinates, new Comparator<List<Integer>>() {
            public int compare(List<Integer> a, List<Integer> b) {
                if (a.get(0).equals(b.get(0))) {
                    return Integer.compare(b.get(1), a.get(1));
                } else {
                    return Integer.compare(a.get(0), b.get(0));
                }
            }
        });

        return coordinates;
    }
}


A: 
