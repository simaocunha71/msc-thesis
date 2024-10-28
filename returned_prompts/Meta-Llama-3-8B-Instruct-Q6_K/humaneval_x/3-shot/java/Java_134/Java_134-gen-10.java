        if (txt.isEmpty()) return false;

        String[] words = txt.split("\\s+");
        if (words.length == 0) return false;

        String lastWord = words[words.length - 1];
        if (lastWord.isEmpty()) return false;

        char lastChar = lastWord.charAt(lastWord.length() - 1);
        return Character.isLetter(lastChar) && !Character.isLetter(lastWord.charAt(lastWord.length() - 2));
    }
}

