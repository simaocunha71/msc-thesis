        String[] words = txt.split("\\s+");
        if (words.length == 0) {
            return txt.replace(",", "").toLowerCase().chars().filter(c -> c >= 'a' && c <= 'z').filter(c -> (c - 'a') % 2 == 1).count();
        } else {
            return Arrays.asList(words);
        }
    }
}

