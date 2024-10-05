    if (n == 1) {
        List<Integer> list = new ArrayList<>();
        list.add(3);
        return list;
    }
    if (n == 2) {
        List<Integer> list = new ArrayList<>();
        list.add(3);
        list.add(2);
        return list;
    }
    if (n == 3) {
        List<Integer> list = new ArrayList<>();
        list.add(3);
        list.add(2);
        list.add(8);
        return list;
    }

    List<Integer> list = new ArrayList<>();
    int i = 3;
    int j = 3;
    int k = 2;
    list.add(3);
    list.add(2);
    list.add(8);
    while (i <= n) {
        if (i % 2 == 0) {
            j += 1;
        } else {
            int tmp = list.get(j);
            tmp += list.get(k);
            tmp += list.get(k + 1);
            list.add(tmp);
            j += 1;
            k += 1;
        }
        i += 1;
    }
    return list;
}

}












































































































































































































