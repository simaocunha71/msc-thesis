        List<Integer> list = new ArrayList<Integer>();
        while (n != 1) {
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
            list.add(n);
        }
        list.add(1);
        return list;
    }
}


