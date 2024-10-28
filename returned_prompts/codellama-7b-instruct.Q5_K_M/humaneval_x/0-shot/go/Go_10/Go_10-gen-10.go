        List<Integer> res = new ArrayList<>();
        for (String s : paren_string.split(" ")) {
            int max = 0;
            int count = 0;
            for (char c : s.toCharArray()) {
                if (c == '(') {
                    count++;
                } else {
                    count--;
                }
                if (count > max) {
                    max = count;
                }
            }
            res.add(max);
        }
        return res;
    }
}
