        int total_chars_1 = lst1.stream().mapToInt(String::length).sum();
        int total_chars_2 = lst2.stream().mapToInt(String::length).sum();

        if (total_chars_1 < total_chars_2) {
            return lst1;
        } else if (total_chars_2 < total_chars_1) {
            return lst2;
        } else {
            return lst1;
        }
    }
}

