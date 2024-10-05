        List<Object> result = new ArrayList<>();
        String rev_s = new StringBuilder(s).reverse().toString();
        StringBuilder sb = new StringBuilder(s);
        for (char ch : c.toCharArray()) {
            sb = sb.replace(sb.toString().indexOf(ch), sb.toString().indexOf(ch) + 1, "");
            sb = new StringBuilder(sb.toString());
            sb.reverse();
        }
        result.add(sb.toString());
        result.add(rev_s.equals(sb.toString()));
        return result;
    }
}

