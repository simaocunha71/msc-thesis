        if (lst1.size() < lst2.size()) {
            return lst1;
        } else if (lst1.size() > lst2.size()) {
            return lst2;
        }

        int total_chars1 = 0;
        int total_chars2 = 0;
        for (String s : lst1) {
            total_chars1 += s.length();
        }
        for (String s : lst2) {
            total_chars2 += s.length();
        }

        if (total_chars1 < total_chars2) {
            return lst1;
        } else if (total_chars1 > total_chars2) {
            return lst2;
        }

        List<String> result = new ArrayList<>();
        for (String s : lst1) {
            result.add(s);
        }
        return result;
    }
}

