        int i = txt.length() - 1;
        while (i >= 0 && Character.isLetter(txt.charAt(i))) {
            i--;
        }
        return i == txt.length() - 1;
    }
}

