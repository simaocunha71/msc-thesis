        StringBuilder result = new StringBuilder();
        char[] chars = s.toCharArray();

        for (char c : chars) {
            result.append((char) (c + 1));
        }
        return result.toString();
    }
}

