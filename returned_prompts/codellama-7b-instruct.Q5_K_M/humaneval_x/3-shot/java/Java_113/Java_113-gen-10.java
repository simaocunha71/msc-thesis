        List<String> result = new ArrayList<>();

        for (String str : lst) {
            int odd_count = 0;

            for (char c : str.toCharArray()) {
                if (Character.getNumericValue(c) % 2 == 1) odd_count += 1;
            }
            result.add("the number of odd elements " + odd_count + "n the str" + odd_count + "ng " + odd_count + " of the " + odd_count + "nput.");
        }
        return result;
    }
}

