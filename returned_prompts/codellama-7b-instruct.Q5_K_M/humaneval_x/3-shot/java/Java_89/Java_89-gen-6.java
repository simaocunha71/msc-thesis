        StringBuilder sb = new StringBuilder();
        String alph = "abcdefghijklmnopqrstuvwxyz";
        for (char c : s.toCharArray()) {
            int i = alph.indexOf(c);
            if (i != -1) {
                i = (i + 2 * 2) % 26;
                sb.append(alph.charAt(i));
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}

