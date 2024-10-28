        int totalChars1 = 0, totalChars2 = 0;

        for (String s : lst1) {
            totalChars1 += s.length();
        }

        for (String s : lst2) {
            totalChars2 += s.length();
        }

        return totalChars1 < totalChars2 ? lst1 : lst2;
    }
}

