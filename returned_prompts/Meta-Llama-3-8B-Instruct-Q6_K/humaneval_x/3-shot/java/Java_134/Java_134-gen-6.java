        String[] words = txt.trim().split("\\s+");
        return !words.isEmpty() && !Character.isLetter(words[words.length - 1].charAt(words[words.length - 1].length() - 1));
    }
}

