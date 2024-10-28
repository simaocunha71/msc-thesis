        StringBuilder result = new StringBuilder();
        for (char c1 : s.toCharArray()) {
            if (!c.contains(String.valueOf(c1))) {
                result.append(c1);
            }
        }
        return Arrays.asList(result.toString(), result.toString().equals(result.reverse().toString()));
    }
}

