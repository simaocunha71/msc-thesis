        List<String> result = new ArrayList<>();
        for (String s: lst) {
            int count = 0;
            for (char c: s.toCharArray()) {
                if ((c - '0') % 2 != 0) {
                    count += 1;
                }
            }
            result.add("the number of odd elements " + count + "n the str" + count + "ng " + count + "f the " + count + "nput.");
        }
        return result;
    }
}

