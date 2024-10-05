        List<Object> result = new ArrayList<>();
        StringBuilder str = new StringBuilder(s);
        for (int i = 0; i < c.length(); i++) {
            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) == c.charAt(i)) {
                    str.deleteCharAt(j);
                    j--;
                }
            }
        }
        if (str.toString().equals(str.toString().replace("", ""))) {
            result.add(str.toString());
            result.add(true);
        } else {
            result.add(str.toString());
            result.add(false);
        }
        return result;
    }
}

