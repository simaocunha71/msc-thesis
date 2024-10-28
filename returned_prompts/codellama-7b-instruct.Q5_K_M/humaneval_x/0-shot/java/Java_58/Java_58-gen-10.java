        List<Integer> list = new ArrayList<Integer>();
        List<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < l1.size(); i++) {
            if (l2.contains(l1.get(i))) {
                list.add(l1.get(i));
                continue A;
            }
        }
        Collections.sort(list);
        for (int i = 0; i < list.size() - 1; i++) {
            if (list.get(i).equals