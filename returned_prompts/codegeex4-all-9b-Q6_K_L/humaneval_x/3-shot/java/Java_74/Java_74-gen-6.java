        int count1 = 0;
        for (String s : lst1) {
            count1 += s.length();
        }

        int count2 = 0;
        for (String s : lst2) {
            count2 += s.length();
        }

        if (count1 < count2) {
            return lst1;
        } else {
            return lst2;
        }
    }
}

