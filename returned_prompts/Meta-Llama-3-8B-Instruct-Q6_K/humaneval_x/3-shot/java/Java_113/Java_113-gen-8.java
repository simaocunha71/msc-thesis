        List<String> result = new ArrayList<>();
        for (String s : lst) {
            int count = 0;
            for (char c : s.toCharArray()) {
                if ((c - '0') % 2 != 0) {
                    count++;
                }
            }
            result.add("the number of odd elements " + count + "n the str" + lst.indexOf(s) + "ng " + s + " of the " + lst.indexOf(s) + "nput.");
        }
        return result;
    }
}

