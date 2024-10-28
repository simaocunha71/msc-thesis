        StringBuilder result = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            char ca = a.charAt(i);
            char cb = (i < b.length()) ? b.charAt(i) : '0';
            result.append((ca == cb ? '0' : '1'));
        }
        return result.toString();
    }
}

