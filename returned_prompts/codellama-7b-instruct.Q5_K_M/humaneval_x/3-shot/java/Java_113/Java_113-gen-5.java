        List<String> result = new ArrayList<>();

        for (String str : lst) {
            int count = 0;
            for (char c : str.toCharArray()) {
                if (Character.getNumericValue(c) % 2 != 0) {
                    count += 1;
                }
            }
            result.add("the number of odd elements " + count + "n the str" + str.length() + "ng " + str.length() + " of the " + lst.size() + "ninput.");
        }
        return result;
    }
}

