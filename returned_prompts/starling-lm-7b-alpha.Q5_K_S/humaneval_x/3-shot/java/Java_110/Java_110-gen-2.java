        int odd_count = 0;
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 == 1) {
                odd_count += 1;
            }
        }
        if (odd_count == 0) return "YES";
        for (int i = 0; i < lst2.size(); i++) {
            if (lst2.get(i) % 2 == 1) {
                odd_count -= 1;
                lst1.set(i, lst2.get(i));
                if (odd_count == 0) return "YES";
            }
        }
        return "NO";
    }
}

