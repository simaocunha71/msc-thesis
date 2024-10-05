        int len1 = 0, len2 = 0;
        for (String s : lst1) {
            len1 += s.length();
        }
        for (String s : lst2) {
            len2 += s.length();
        }
        if (len1 < len2) return lst1;
        return lst2;
    }
}

