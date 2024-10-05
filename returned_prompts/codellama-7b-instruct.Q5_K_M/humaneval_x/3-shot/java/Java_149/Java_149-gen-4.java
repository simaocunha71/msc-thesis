        lst.removeIf(word -> word.length() % 2 != 0);
        lst.sort((a, b) -> {
            if (a.length() == b.length()) return a.compareTo(b);
            return a.length() - b.length();
        });
        return lst;
    }
}

