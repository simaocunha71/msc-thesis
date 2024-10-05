    List<Integer> list = new ArrayList<Integer>();
    if(n == 1) {
        list.add(n);
        return list;
    }
    if(n % 2 == 0) {
        list.add(n);
        n = n + 1;
    } else {
        list.add(n);
        n = n + 2;
    }
    for(int i = 1; i < n; i++) {
        if(n % 2 == 0 && i % 2 != 0) {
            list.add(n);
            n = n + 2;
        } else if(n % 2 != 0 && i % 2 == 0) {
            list.add(n);
            n = n + 2;
        } else if(n % 2 != 0 && i % 2 != 0) {
            list.add(n);
            n = n + 1;
        } else if(n % 2 == 0 && i % 2 == 0) {
            list.add(n);
            n = n + 1;
        }
    }
    return list;
    }
}



































































































































































































































