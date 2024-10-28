        if (txt.isEmpty()) return false;
        String[] words = txt.split("\\s+");
        return words[words.length - 1].length() > 0 && !Character.isLetter(words[words.length - 1].charAt(words[words.length - 1].length() - 1));
    }
}

