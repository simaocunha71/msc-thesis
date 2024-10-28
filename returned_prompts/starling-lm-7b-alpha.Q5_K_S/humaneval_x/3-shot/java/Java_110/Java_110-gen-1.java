        int odd_count = 0;
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 == 0) {
                odd_count += 1;
            }
        }
        if (odd_count == lst1.size()) {
            return "NO";
        }

        for (int i = 0; i < lst2.size(); i++) {
            if (lst2.get(i) % 2 == 0 && odd_count > 0) {
                lst1.set(lst1.size() - odd_count, lst2.get(i));
                odd_count -= 1;
            }
        }
        return "YES";
    }
}

