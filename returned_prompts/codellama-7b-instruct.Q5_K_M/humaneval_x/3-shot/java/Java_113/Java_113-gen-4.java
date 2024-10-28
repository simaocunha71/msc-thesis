        List<String> result = new ArrayList<>();
        for (String s : lst) {
            int count = 0;
            for (char c : s.toCharArray()) {
                if (Character.getNumericValue(c) % 2 == 1) {
                    count++;
                }
            }
            result.add("the number of odd elements " + count + "n the str" + (count % 10) + "ng " + (count / 10) + " of the " + (count % 10) + "nput.");
        }
        return result;
    }
}

