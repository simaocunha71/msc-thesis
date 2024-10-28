        if (txt.isEmpty()) return false;

        int index = txt.length() - 1;
        while (index >= 0 && Character.isWhitespace(txt.charAt(index))) {
            index--;
        }
        return index >= 0 && Character.isLetter(txt.charAt(index));
    }
}

