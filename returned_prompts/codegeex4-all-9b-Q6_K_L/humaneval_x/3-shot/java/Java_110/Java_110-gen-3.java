        int even1 = 0;
        int even2 = 0;
        for (int i : lst1) {
            if (i % 2 == 0) even1 += 1;
        }
        for (int i : lst2) {
            if (i % 2 == 0) even2 += 1;
        }
        return even1 + even2 >= lst1.size() ? "YES" : "NO";
    }
}

