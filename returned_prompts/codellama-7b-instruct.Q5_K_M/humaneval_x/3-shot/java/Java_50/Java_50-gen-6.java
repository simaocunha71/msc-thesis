        return new String(s.replaceAll("\\w", m -> (char) ('a' + (m.group(0).charAt(0) - 'a' + 26) % 26)));
    }
}

