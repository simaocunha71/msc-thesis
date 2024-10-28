        int odd_count_1 = 0;
        int odd_count_2 = 0;

        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 != 0) odd_count_1 += 1;
        }

        for (int i = 0; i < lst2.size(); i++) {
            if (lst2.get(i) % 2 != 0) odd_count_2 += 1;
        }

        if (odd_count_1 == 0) return "YES";
        else if (odd_count_2 == 0) return "NO";

        return odd_count_1 <= odd_count_2 ? "YES" : "NO";

    }
}

