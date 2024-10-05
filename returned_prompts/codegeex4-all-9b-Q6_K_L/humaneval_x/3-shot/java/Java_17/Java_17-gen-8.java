        List<Integer> result = new ArrayList<>();
        for (char c : string.toCharArray()) {
            if (c == 'o') {
                result.add(4);
            } else if (c == '.') {
                result.add(1);
            } else if (c == '|') {
                result.add(2);
            }
        }
        return result;
    }
}

