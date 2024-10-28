        if (lst1.size() == lst2.size()) {
            return lst1;
        }

        int total_chars = 0;
        for (String s : lst1) {
            total_chars += s.length();
        }
        for (String s : lst2) {
            total_chars += s.length();
        }

        int smaller_total = Integer.MAX_VALUE;
        List<String> smaller_lst = null;

        if (lst1.size() < lst2.size()) {
            smaller_total = total_chars - lst1.size();
            smaller_lst = lst1;
        } else {
            smaller_total = total_chars - lst2.size();
            smaller_lst = lst2;
        }

        return smaller_lst;

    }
}

