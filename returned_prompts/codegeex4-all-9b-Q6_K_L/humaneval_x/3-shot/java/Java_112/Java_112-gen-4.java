        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (!c.contains(String.valueOf(ch))) {
                sb.append(ch);
            }
        }
        return Arrays.asList(sb.toString(), sb.toString().equals(sb.reverse().toString()));
    }
}

