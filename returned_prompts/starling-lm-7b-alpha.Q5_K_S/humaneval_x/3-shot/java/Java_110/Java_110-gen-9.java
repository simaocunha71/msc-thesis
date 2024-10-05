        int odd_count = 0;
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 == 0) continue;
            odd_count += 1;
            if (odd_count > lst2.size()) return "NO";
            for (int j = 0; j < lst2.size(); j++) {
                if (lst2.get(j) % 2 == 0) {
                    lst1.set(i, lst2.get(j));
                    lst2.set(j, lst1.get(i));
                    return "YES";
                }
            }
        }
        return "NO";
    }
}

