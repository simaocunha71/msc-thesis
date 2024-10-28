        List<Integer> list = new ArrayList<Integer>();
        list.add(n);
        while (list.get(list.size()-1) != 1) {
            if (list.get(list.size()-1) % 2 == 0) {
                list.add(list.get(list.size()-1) / 2);
            } else {
                list.add(list.get(list.size()-1) * 3 + 1);
            }
        }
        Collections.sort(list);
        return list;
    }
}
