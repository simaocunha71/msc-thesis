        int lst1_total_chars = 0;
        int lst2_total_chars = 0;
        for (String s : lst1) {
            lst1_total_chars += s.length();
        }
        for (String s : lst2) {
            lst2_total_chars += s.length();
        }
        if (lst1_total_chars < lst2_total_chars) {
            return lst1;
        } else if (lst1_total_chars > lst2_total_chars) {
            return lst2;
        } else {
            return lst1;
        }

    }
}

