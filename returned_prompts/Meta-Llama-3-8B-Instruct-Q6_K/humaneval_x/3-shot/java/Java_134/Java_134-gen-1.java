        String[] words = txt.split("\\s+");
        if (words.length == 0) return false;
        String lastWord = words[words.length - 1];
        return !lastWord.isEmpty() && !Character.isLetter(lastWord.charAt(lastWord.length() - 1));
    }
}

