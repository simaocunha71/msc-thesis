        if (lst1.size() == 0 || lst2.size() == 0) return lst1.size() < lst2.size() ? lst1 : lst2;

        int totalChar1 = 0;
        for (String s : lst1) totalChar1 += s.length();
        int totalChar2 = 0;
        for (String s : lst2) totalChar2 += s.length();

        if (totalChar1 == totalChar2) return lst1;

        if (totalChar1 > totalChar2) return lst2;
        else return lst1;
    }
}

