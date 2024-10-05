        int even = 0;
        int odd = 0;
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 == 0) even += 1;
            else odd += 1;
        }
        for (int i = 0; i < lst2.size(); i++) {
            if (lst2.get(i) % 2 == 0) even += 1;
            else odd += 1;
        }
        if (odd <= even) return "YES";
        else return "NO";
    }
}

