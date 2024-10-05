        int depth = 0;

        for (char c : string.toCharArray()) {
            if (c == '[') depth += 1;
            else depth -= 1;

            if (depth == 0) return true;
        }
        return false;
    }
}

