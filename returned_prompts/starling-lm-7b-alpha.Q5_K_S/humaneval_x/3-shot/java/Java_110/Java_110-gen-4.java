        int even_count = 0;
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 == 0) {
                even_count += 1;
            }
        }

        if (even_count == lst1.size()) {
            return "YES";
        }

        for (int i = 0; i < lst2.size(); i++) {
            if (lst2.get(i) % 2 == 0) {
                if (even_count < lst1.size()) {
                    lst1.set(even_count, lst2.get(i));
                    even_count += 1;
                } else {
                    return "YES";
                }
            }
        }
        return "NO";
    }
}

```