        List<String> result = new ArrayList<>();
        for (String s : lst) {
            int count = 0;
            for (char c : s.toCharArray()) {
                if (c % 2 != 0) count += 1;
            }
            result.add("the number of odd elements " + count + "n the str" + s.length() + "ng " + s.length() + " of the " + s.length() + "nput.");
        }
        return result;
    }
}

