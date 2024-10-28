        List<Integer> list = new ArrayList();
        for (int i = 0; i < l1.size(); i++) {
            for (int j = 0; j < l2.size(); j++) {
                if (l1.get(i).equals(l2.get(j))) {
                    list.add(l1.get(i));
                    continue A;
                }
            }
        }
        Collections.sort(list);
        return list;
    }
}
