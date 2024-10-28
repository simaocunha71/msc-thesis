        String[] words = txt.split("\\s+");
        if (words.length > 0) return Arrays.asList(words);
        else return txt.split(",");
    }
}

