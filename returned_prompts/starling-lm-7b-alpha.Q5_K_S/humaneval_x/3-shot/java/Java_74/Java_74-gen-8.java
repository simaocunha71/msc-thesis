        if (lst1.size() < lst2.size()) return lst1;
        if (lst1.size() > lst2.size()) return lst2;
        int sum_lst1 = 0;
        int sum_lst2 = 0;
        for (String s : lst1) {
            sum_lst1 += s.length();
        }
        for (String s : lst2) {
            sum_lst2 += s.length();
        }
        if (sum_lst1 < sum_lst2) return lst1;
        if (sum_lst2 < sum_lst1) return lst2;
        return lst1;
    }
}

