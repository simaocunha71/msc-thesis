        if(txt.isEmpty())
            return false;
        String[] words = txt.split(" ");
        String lastWord = words[words.length - 1];
        if(lastWord.length() == 0)
            return false;
        char lastChar = lastWord.charAt(lastWord.length() - 1);
        return Character.isLetter(lastChar);
    }
}

