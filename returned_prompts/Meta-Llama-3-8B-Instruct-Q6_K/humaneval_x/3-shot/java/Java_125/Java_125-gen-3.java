        String[] words = txt.split("\\s+");
        if (words.length == 1) {
            return txt.split(",").length;
        } else {
            return Arrays.asList(words);
        }
    }
}

