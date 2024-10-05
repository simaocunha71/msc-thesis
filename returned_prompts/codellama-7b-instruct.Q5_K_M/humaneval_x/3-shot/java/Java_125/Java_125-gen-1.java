        String[] words = txt.split("\\s+");
        if (words.length > 0) {
            return words;
        } else if (txt.matches(".*\\d.*")) {
            return Integer.parseInt(txt);
        } else {
            return txt.length();
        }
    }
}

