        int total_chars1 = lst1.stream().mapToInt(String::length).sum();
        int total_chars2 = lst2.stream().mapToInt(String::length).sum();

        if (total_chars1 < total_chars2) return lst1;
        if (total_chars1 > total_chars2) return lst2;

        return lst1;
    }
}

