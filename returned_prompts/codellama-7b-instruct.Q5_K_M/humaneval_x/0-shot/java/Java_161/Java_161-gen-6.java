        return s.chars().mapToObj(c -> (char) c).map(c -> c.isLetter() ? Character.isUpperCase(c) ? Character.toLowerCase(c) : Character.toUpperCase(c) : c).collect(Collectors.joining());
    }
}






















