        String[] words = txt.split("\\s+");
        if (words.length == 0) {
            return txt.split(",").length;
        } else {
            return Arrays.asList(words);
        }
    }
}

