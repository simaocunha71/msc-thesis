        List<String> even_length_list = new ArrayList<>();
        for  (String s  : lst) {
            if (s.length() % 2 == 0) {
                even_length_list.add(s);
            }
        }
        Collections.sort(even_length_list);
        return even_length_list;
    }
}

