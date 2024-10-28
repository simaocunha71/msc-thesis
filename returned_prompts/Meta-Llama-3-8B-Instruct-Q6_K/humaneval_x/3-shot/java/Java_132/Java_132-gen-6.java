        int countOpen = 0;
        for (char c : string.toCharArray()) {
            if (c == '[') {
                countOpen++;
            } else if (c == ']') {
                if (countOpen == 0) return false;
                countOpen--;
            }
        }
        return countOpen > 0;
    }
}

