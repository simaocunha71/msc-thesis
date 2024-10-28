        // return lst;
        // return lst.stream().filter(wrd -> wrd.length() % 2 == 0).sorted((a, b) -> (a.length() - b.length())).collect(Collectors.toList());
        return lst.stream().filter(wrd -> wrd.length() % 2 == 0).sorted((a, b) -> (a.length() - b.length())).collect(Collectors.toList());
    }
}
