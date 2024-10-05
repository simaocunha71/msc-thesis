        StringBuilder result = new StringBuilder();
        char[] chars = s.toCharArray();
        for (char c : chars) {
            if (Character.isLetter(c)) {
                if (Character.isLowerCase(c)) result.append(Character.toUpperCase(c));
                else result.append(Character.toLowerCase(c));
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

