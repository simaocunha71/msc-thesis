        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < string.length(); i++) {
            switch (string.charAt(i)) {
                case 'o':
                    result.add(4);
                    break;
                case '|':
                    result.add(2);
                    break;
                case '.':
                    result.add(1);
                    break;
            }
        }
        return result;
    }
}
