        List<String> result = new ArrayList<>();
        for (String s : lst) {
            int count = 0;
            for (char c : s.toCharArray()) {
                if (c - '0' % 2 == 1) count++;
            }
            result.add("the number of odd elements " + count + "n the str" + (s.length() % 10) + "ng " + (s.length() % 10) + " of the " + (s.length() % 10) + "nput.");
        }
        return result;
    }
}

