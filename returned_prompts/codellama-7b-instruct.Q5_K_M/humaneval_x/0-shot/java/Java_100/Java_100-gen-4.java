        List<Integer> list = new ArrayList<Integer>();
        int i = 1;
        while (i <= n) {
            list.add(i);
            if (n % 2 == 1) {
                i += 2;
            } else {
                i += 1;
            }
        }
        return list;
    }
}
