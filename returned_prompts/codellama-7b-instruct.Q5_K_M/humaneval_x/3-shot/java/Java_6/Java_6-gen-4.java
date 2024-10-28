        List<Integer> result = new ArrayList<>();
        int depth = 0;

        for (String group : paren_string.split(" ")) {
            int d = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') d += 1;
                else d -= 1;
            }
            result.add(d);
        }
        return result;
    }
}

