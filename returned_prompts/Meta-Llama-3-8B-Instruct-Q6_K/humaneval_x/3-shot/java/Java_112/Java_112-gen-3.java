        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (char c1 : s.toCharArray()) {
            if (!c.contains(String.valueOf(c1))) {
                sb.append(c1);
            }
        }
        result.add(sb.toString());
        result.add(sb.toString().equals(new StringBuilder(sb.toString()).reverse().toString()));
        return result;
    }
}

