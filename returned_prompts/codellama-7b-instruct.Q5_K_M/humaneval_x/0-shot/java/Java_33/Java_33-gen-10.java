        List<Integer> newList = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                list.add(l.get(i));
            }
            if (i % 3 == 1) {
                list2.add(l.get(i));
            }
        }
        newList.addAll(list);
        newList.addAll(list2);
        Collections.sort(newList);
        return newList;
    }
}

