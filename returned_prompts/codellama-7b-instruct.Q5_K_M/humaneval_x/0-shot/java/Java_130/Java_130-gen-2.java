        List<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(3);
        list.add(2);
        list.add(8);

        for (int i = 4; i <= n; i++) {
            list.add(list.get(i - 1) + list.get(i - 2) + list.get(i - 3));
        }
        return list;
    }
}
