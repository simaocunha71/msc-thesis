        List<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < string.length(); i++) {
            if (string.charAt(i) == 'o') {
                list.add(4);
            } else if (string.charAt(i) == '|') {
                list.add(2);
            } else if (string.charAt(i) == '.') {
                list.add(1);
            }
        }
        return list;
    }
}
