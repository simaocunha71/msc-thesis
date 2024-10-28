        for (int i = 0; i < lst1.size(); i++) {
            for (int j = 0; j < lst2.size(); j++) {
                if (lst1.get(i) % 2 == 0 && lst2.get(j) % 2 != 0) {
                    int temp = lst1.get(i);
                    lst1.set(i, lst2.get(j));
                    lst2.set(j, temp);
                }
            }
        }

        for (int i : lst1) {
            if (i % 2 != 0) {
                return "NO";
            }
        }
        return "YES";
    }
}

