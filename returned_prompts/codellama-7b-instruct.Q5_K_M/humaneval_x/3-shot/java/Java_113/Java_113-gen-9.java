        List<String> result = new ArrayList<>();
        for (String s : lst) {
            int odd = 0;
            for (char c : s.toCharArray()) {
                if (Integer.valueOf(c + "") % 2 != 0) odd++;
            }
            result.add("the number of odd elements " + odd + "n the str" + odd + "ng " + (result.size() + 1) + " of the " + (result.size() + 1) + "nput.");
        }
        return result;
    }
}

