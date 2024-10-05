        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 != 0) {
                result.add(l.get(i));
            } else {
                result.add(sortedGet(l, i));
            }
        }
        return result;
    }

    private int sortedGet(List<Integer> l, int index) {
        List<Integer> temp = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == index % 3) {
                temp.add(l.get(i));
            }
        }
        Collections.sort(temp);
        return temp.get(0);
    }
}

