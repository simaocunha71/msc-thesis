        int even_count = 0;
        for (int i : lst1) {
            if (i % 2 == 0) {
                even_count += 1;
            }
        }

        if (even_count == lst1.size()) {
            return "YES";
        }

        for (int i = 0; i < lst2.size(); i++) {
            if (lst2.get(i) % 2 == 0) {
                even_count += 1;
                if (even_count == lst1.size()) {
                    return "YES";
                }
            }
        }
        return "NO";
    }
}

