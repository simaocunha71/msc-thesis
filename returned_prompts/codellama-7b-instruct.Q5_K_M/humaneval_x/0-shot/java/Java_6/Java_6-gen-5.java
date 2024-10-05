        List<Integer> result = new ArrayList<Integer>();
        String[] groups = paren_string.split(" ");
        for (String group : groups) {
            int level = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') level++;
                else if (c == ')') level--;
                if (level < 0) break;
            }
            result.add(level);
        }
        return result;
    }
}

