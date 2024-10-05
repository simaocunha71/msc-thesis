        int odd1 = 0, even2 = 0;
        for (int i : lst1) {
            if (i % 2 != 0) {
                odd1++;
            }
        }
        for (int i : lst2) {
            if (i % 2 == 0) {
                even2++;
            }
        }
        return odd1 <= even2 ? "YES" : "NO";
     }
}

