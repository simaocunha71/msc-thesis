        List<Integer> result = new ArrayList<>();
        for (char c : string.toCharArray()) {
            switch (c) {
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

