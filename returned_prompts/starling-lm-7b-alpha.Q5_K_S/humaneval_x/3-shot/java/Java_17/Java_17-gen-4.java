        List<Integer> result = new ArrayList<>();
        int duration = 0;
        for (char c : string.toCharArray()) {
            switch (c) {
                case 'o':
                    duration = 4;
                    break;
                case 'o|':
                    duration = 2;
                    break;
                case '.':
                    duration = 1;
                    break;
                default:
                    break;
            }
            result.add(duration);
        }
        return result;
    }
}

