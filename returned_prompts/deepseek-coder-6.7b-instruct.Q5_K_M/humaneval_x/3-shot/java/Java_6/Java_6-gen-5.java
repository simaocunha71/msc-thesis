        List<Integer> result = new ArrayList<>();
        String[] groups = paren_string.split(" ");
        for (String group : groups) {
            int count = 0;
            int max = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    count++;
                    if (count > max) {
                        max = count;
                    }
                } else if (c == ')') {
                    count--;
                }
            }
            result.add(max);
        }
        return result;
    }
}

