        return (txt.length() > 0 && Character.isAlphabetic(txt.charAt(txt.length() - 1)) &&
                Character.isWhitespace(txt.charAt(txt.length() - 2)));
    }
}

