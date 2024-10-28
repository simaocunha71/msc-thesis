        int even_count = 0;
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 == 0) {
                even_count += 1;
            }
        }
        if (even_count == lst1.size()) return "YES";

        for (int i = 0; i < lst2.size(); i++) {
            if (lst2.get(i) % 2 == 0) {
                lst1.set(lst1.size() - 1, lst2.get(i));
                lst2.remove(i);
                i -= 1;
            }
        }
        if (lst1.size() == 0) return "YES";
        return "NO";
    }
}

