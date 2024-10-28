        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder(s);
        for (int i = 0; i < sb.length(); i++) {
            char current = sb.charAt(i);
            if (!c.contains(String.valueOf(current))) {
                result.add(current);
            }
        }
        StringBuilder reversed = new StringBuilder(String.join("", Collections.reverse(result)));
        result.add(reversed.toString().equals(sb.toString()));
        return result;

    }
}

