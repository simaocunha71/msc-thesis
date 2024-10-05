        int total_chars_lst1 = 0;
        for (String s : lst1) {
            total_chars_lst1 += s.length();
        }
        int total_chars_lst2 = 0;
        for (String s : lst2) {
            total_chars_lst2 += s.length();
        }
        if (total_chars_lst1 > total_chars_lst2) {
            return lst2;
        } else if (total_chars_lst1 < total_chars_lst2) {
            return lst1;
        } else {
            return lst1;
        }
    }
}

