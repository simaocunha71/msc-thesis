        List<Integer> list = new ArrayList<>();

        for (int i = 0; i < string.length(); i++) {
            if (string.charAt(i) == 'o') {
                list.add(4);
            } else if (string.charAt(i) == '|') {
                if (string.charAt(i + 1) == 'o') {
                    list.add(2);
                } else if (string.charAt(i + 1) == '.') {
                    list.add(1);
                }
            }
        }
        return list;
    }
}
