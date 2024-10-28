        int odd_in_lst1 = 0;
        for (int num : lst1) {
            if (num % 2 == 1) odd_in_lst1 += 1;
        }

        int even_in_lst2 = 0;
        for (int num : lst2) {
            if (num % 2 == 0) even_in_lst2 += 1;
        }

        if (odd_in_lst1 <= even_in_lst2) return "YES";
        return "NO";
    }
}

