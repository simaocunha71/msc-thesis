        if (txt.length() == 0) return false;
        char lastChar = txt.charAt(txt.length() - 1);
        return Character.isLetter(lastChar) && !Character.isLetter(txt.charAt(txt.length() - 2));
     }
}

