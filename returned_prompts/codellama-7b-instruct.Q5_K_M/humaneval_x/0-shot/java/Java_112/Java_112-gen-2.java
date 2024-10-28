        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (!c.contains(String.valueOf(ch))) {
                sb.append(ch);
            }
        }
        result.add(sb.toString());
        result.add(sb.toString().equals(sb.reverse().toString()));
        return result;
    }
}



