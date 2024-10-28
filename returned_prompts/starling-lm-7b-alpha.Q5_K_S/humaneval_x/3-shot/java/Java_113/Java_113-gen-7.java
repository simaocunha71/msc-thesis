        List<String> result = new ArrayList<>();
        for (String s : lst) {
            int odd_count = 0;
            for (char c : s.toCharArray()) {
                if (c % 2 != 0) odd_count += 1;
            }
            result.add("the number of odd elements " + odd_count + "n the str" + odd_count + "ng " + odd_count + "f the " + odd_count + "nput.");
        }
        return result;
    }
}

