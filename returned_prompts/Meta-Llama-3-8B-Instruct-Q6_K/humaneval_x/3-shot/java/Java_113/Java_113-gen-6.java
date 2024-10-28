        List<String> result = new ArrayList<>();
        for (String str : lst) {
            int count = 0;
            for (char c : str.toCharArray()) {
                if ((c - '0') % 2 != 0) {
                    count++;
                }
            }
            result.add("the number of odd elements " + count + "n the str" + (lst.indexOf(str) + 1) + "ng " + (lst.indexOf(str) + 1) + " of the " + (lst.indexOf(str) + 1) + "nput.");
        }
        return result;
    }
}

