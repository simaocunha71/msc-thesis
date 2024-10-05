        List<Integer> result = new ArrayList<>();
        for (char c : string.toCharArray()) {
            if (c == 'o') {
                result.add(4);
            } else if (c == '|') {
                result.add(0);
            } else if (c == '.') {
                result.add(1);
            }
        }
        return result;
    }
}

