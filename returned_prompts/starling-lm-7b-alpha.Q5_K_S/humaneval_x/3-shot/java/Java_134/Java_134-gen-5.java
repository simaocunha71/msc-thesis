        if (txt.isEmpty()) return false;

        if (txt.length() == 1) {
            return Character.isAlphabetic(txt.charAt(0));
        } else {
            return Character.isAlphabetic(txt.charAt(txt.length() - 1)) &&
                txt.charAt(txt.length() - 1) != txt.charAt(txt.lastIndexOf(' ') + 1);
        }
    }
}

