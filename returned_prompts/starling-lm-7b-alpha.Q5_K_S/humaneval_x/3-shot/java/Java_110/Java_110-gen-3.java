        int odd_count = 0;
        for (Integer i : lst1) {
            if (i % 2 != 0) odd_count += 1;
        }
        if (odd_count == 0) return "YES";
        for (Integer i : lst2) {
            if (i % 2 != 0) {
                lst1.set(lst1.indexOf(i), i);
                lst2.remove(i);
                odd_count = 0;
                for (Integer j : lst1) {
                    if (j % 2 != 0) odd_count += 1;
                }
                if (odd_count == 0) return "YES";
            }
        }
        return "NO";
    }
}

