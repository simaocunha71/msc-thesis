        int count = 0;
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 == 1) {
                for (int j = 0; j < lst2.size(); j++) {
                    if (lst2.get(j) % 2 == 0) {
                        count += 1;
                        break;
                    }
                }
            }
        }
        return count == lst1.size() ? "YES" : "NO";
    }
}

