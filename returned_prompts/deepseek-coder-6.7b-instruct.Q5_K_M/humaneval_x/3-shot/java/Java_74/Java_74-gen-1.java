        int totalChars1 = 0;
        int totalChars2 = 0;

        for (String s : lst1) {
            totalChars1 += s.length();
        }

        for (String s : lst2) {
            totalChars2 += s.length();
        }

        if (totalChars1 < totalChars2) {
            return lst1;
        } else if (totalChars2 < totalChars1) {
            return lst2;
        } else {
            return lst1;
        }
    }
}

