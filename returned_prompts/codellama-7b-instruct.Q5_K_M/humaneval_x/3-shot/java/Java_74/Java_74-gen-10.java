        int totalChars1 = 0;
        for (String s : lst1) totalChars1 += s.length();

        int totalChars2 = 0;
        for (String s : lst2) totalChars2 += s.length();

        if (totalChars1 < totalChars2) return lst1;
        else if (totalChars1 > totalChars2) return lst2;
        else return lst1;
    }
}

