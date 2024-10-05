        if (lst1.size() < lst2.size()) {
            List<Integer> temp = lst1;
            lst1 = lst2;
            lst2 = temp;
        }

        int lst1_size = lst1.size();
        int lst2_size = lst2.size();

        int lst1_even_count = 0;
        for (int i = 0; i < lst1_size; i++) {
            if (lst1.get(i) % 2 == 0) lst1_even_count += 1;
        }

        int lst2_even_count = 0;
        for (int i = 0; i < lst2_size; i++) {
            if (lst2.get(i) % 2 == 0) lst2_even_count += 1;
        }

        if (lst1_even_count >= lst2_even_count) return "YES";
        else return "NO";
    }
}

