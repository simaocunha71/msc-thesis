        int total_chars = 0;
        for (String s : lst1) {
            total_chars += s.length();
        }
        int total_chars_other = 0;
        for (String s : lst2) {
            total_chars_other += s.length();
        }
        if (total_chars_other < total_chars) return lst2;
        else return lst1;
    }
}

