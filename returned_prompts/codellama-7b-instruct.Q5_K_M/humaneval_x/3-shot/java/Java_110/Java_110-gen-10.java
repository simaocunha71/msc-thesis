        if (lst1.size() != lst2.size()) return "NO";
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 != 0) {
                for (int j = 0; j < lst2.size(); j++) {
                    if (lst2.get(j) % 2 == 0) {
                        int temp = lst1.get(i);
                        lst1.set(i, lst2.get(j));
                        lst2.set(j, temp);
                        break;
                    }
                }
            }
        }
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 != 0) return "NO";
        }
        return "YES";
    }
}

