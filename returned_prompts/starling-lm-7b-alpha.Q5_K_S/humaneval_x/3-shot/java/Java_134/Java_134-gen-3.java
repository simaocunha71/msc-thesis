        return txt.length() > 0 && Character.isAlphabetic(txt.charAt(txt.length() - 1)) && !" ".equals(txt.substring(txt.lastIndexOf(' ') + 1, txt.length()));
    }
}

