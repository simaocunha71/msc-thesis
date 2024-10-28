        if (lst1.size() < lst2.size()) {
            return lst1;
        } else if (lst2.size() < lst1.size()) {
            return lst2;
        }

        int total_chars = 0;
        for (String str : lst1) {
            total_chars += str.length();
        }

        int total_chars2 = 0;
        for (String str : lst2) {
            total_chars2 += str.length();
        }

        if (total_chars < total_chars2) {
            return lst1;
        } else if (total_chars > total_chars2) {
            return lst2;
        }

        List<String> result = new ArrayList<>();
        for (String str : lst1) {
            result.add(str);
        }
        return result;
    }
}

