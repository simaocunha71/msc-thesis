        int even_count = 0;
        for (int i : lst1) {
            if (i % 2 == 0) {
                even_count += 1;
            }
        }
        if (even_count == lst1.size()) {
            return "YES";
        }
        for (int i : lst2) {
            if (i % 2 == 0) {
                if (even_count < lst1.size()) {
                    even_count += 1;
                    lst1.set(even_count - 1, i);
                } else {
                    break;
                }
            }
        }
        if (even_count == lst1.size()) {
            return "YES";
        }
        return "NO";
    }
}

