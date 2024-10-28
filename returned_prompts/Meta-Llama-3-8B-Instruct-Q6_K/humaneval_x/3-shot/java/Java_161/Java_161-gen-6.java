        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                sb.append((char) (Character.toUpperCase(c)));
            } else {
                sb.append(c);
            }
        }
        return sb.reverse().toString();
    }
}

