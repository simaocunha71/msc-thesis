        int even1 = 0;
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 != 0) {
                even1 += 1;
            }
        }

        int even2 = 0;
        for (int i = 0; i < lst2.size(); i++) {
            if (lst2.get(i) % 2 != 0) {
                even2 += 1;
            }
        }

        if (even1 <= even2) {
            return "YES";
        } else {
            return "NO";
        }
    }
}

