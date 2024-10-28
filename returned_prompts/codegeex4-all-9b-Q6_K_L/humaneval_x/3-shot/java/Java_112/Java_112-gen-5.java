        StringBuilder sb = new StringBuilder();

        for (char x : s.toCharArray()) {
            if (!c.contains(String.valueOf(x))) {
                sb.append(x);
            }
        }

        return Arrays.asList(sb.toString(), sb.toString().equals(new StringBuilder(sb).reverse().toString()));
    }
}

