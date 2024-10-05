        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            sb.insert(0, s.charAt(i));
            if (i % 3 == 2 && i != s.length() - 1) {
                sb.setCharAt(0, s.charAt(i + 1));
                sb.deleteCharAt(1);
            }
        }
        return sb.toString();
    }
}

