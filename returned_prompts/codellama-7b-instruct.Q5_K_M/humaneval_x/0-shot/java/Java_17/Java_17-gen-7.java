        List<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < string.length(); i++) {
            switch (string.charAt(i)) {
                case 'o':
                    list.add(4);
                    break;
                case '|':
                    list.add(2);
                    break;
                case '.':
                    list.add(1);
                    break;
            }
        }
        return list;
    }
}
