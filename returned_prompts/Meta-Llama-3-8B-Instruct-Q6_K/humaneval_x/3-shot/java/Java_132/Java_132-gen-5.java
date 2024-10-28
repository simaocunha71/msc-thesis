        int openCount = 0;
        int closeCount = 0;

        for (char c : string.toCharArray()) {
            if (c == '[') {
                openCount++;
            } else if (c == ']') {
                closeCount++;
            }

            if (closeCount > openCount) {
                return true;
            }
        }
        return false;
    }
}

