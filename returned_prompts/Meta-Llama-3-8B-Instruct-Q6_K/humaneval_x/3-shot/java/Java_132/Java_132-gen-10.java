        int openBrackets = 0;
        for (char c : string.toCharArray()) {
            if (c == '[') openBrackets++;
            if (c == ']') {
                if (openBrackets == 0) return true;
                openBrackets--;
            }
        }
        return false;
    }
}

