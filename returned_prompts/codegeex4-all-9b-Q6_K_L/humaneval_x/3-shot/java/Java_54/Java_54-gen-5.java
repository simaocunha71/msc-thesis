        return s0.length() == s1.length() && s0.chars().filter(ch -> s1.indexOf(ch) != -1).count() == s0.length();
    }
}

