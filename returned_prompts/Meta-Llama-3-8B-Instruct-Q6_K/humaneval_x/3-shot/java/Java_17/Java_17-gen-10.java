        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < string.length(); i++) {
            if (string.charAt(i) == 'o') {
                result.add(4);
            } else if (string.charAt(i) == '|') {
                if (i + 1 < string.length() && string.charAt(i + 1) == '.') {
                    result.add(1);
                    i++;
                } else {
                    result.add(2);
                }
            }
        }
        return result;
    }
}

