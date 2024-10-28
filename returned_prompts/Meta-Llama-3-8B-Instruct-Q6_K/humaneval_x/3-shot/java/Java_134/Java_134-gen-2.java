        if (txt.isEmpty()) return false;
        String[] words = txt.split("\\s+");
        if (words[words.length - 1].isEmpty()) return txt.charAt(txt.length() - 1) >= 'a' && txt.charAt(txt.length() - 1) <= 'z';
        return txt.charAt(txt.length() - 1) >= 'a' && txt.charAt(txt.length() - 1) <= 'z';
    }
}

