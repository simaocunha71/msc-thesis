        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (char c1 : s.toCharArray()) {
            boolean is_c = false;
            for (char c2 : c.toCharArray()) {
                if (c1 == c2) {
                    is_c = true;
                    break;
                }
            }
            if (!is_c) {
                sb.append(c1);
            }
        }
        result.add(sb.toString());
        result.add(sb.toString().equals(new StringBuilder(sb.toString().reverse().toString()).toString()));
        return result;
    }
}

