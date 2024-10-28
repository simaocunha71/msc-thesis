        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder(s);
        for (int i = sb.length() - 1; i >= 0; i--) {
            boolean found = false;
            for (int j = 0; j < c.length(); j++) {
                if (sb.charAt(i) == c.charAt(j)) {
                    sb.deleteCharAt(i);
                    found = true;
                    break;
                }
            }
            if (!found) {
                result.add(sb.toString());
                result.add(sb.toString().equals(new StringBuilder(sb.toString()).reverse().toString()));
                return result;
            }
        }
        result.add(sb.toString());
        result.add(false);
        return result;
    }
}

