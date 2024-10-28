        return a.contains(b) || a.contains(reverse(b)) || a.contains(b.substring(1)) || a.contains(reverse(b.substring(1)));
    }

    private String reverse(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = s.length() - 1; i >= 0; i--) {
            sb.append(s.charAt(i));
        }
        return sb.toString();
    }
}

