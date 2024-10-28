        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 == 1) {
                for (int j = 0; j < lst2.size(); j++) {
                    if (lst2.get(j) % 2 == 0) {
                        lst1.set(i, lst2.get(j));
                        lst2.set(j, lst1.get(i));
                        break;
                    }
                }
            }
        }

        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 == 1) {
                return "NO";
            }
        }

        return "YES";
    }
}

