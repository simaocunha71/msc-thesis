        List<Integer> list = new ArrayList();
        for (int i = 0; i < string.length(); i++) {
            char c = string.charAt(i);
            if (c == 'o') {
                list.add(4);
            } else if (c == 'o' && string.charAt(i + 1) == '|') {
                list.add(2);
                i++;
            } else if (c == '.' && string.charAt(i + 1) == '|') {
                list.add(1);
                i++;
            } else {
                continue A;
            }
        }
        return list;
    }
}

