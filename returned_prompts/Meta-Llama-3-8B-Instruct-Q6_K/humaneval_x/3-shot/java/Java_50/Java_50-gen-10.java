        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            sb.append((char) ('a' + ((ch - 'a' + 26) % 26)));
        }
        return sb.toString();
    }
}