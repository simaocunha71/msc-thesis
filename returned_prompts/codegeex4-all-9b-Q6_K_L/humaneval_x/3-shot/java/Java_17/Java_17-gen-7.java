        List<Integer> result = new ArrayList<>();
        String[] tokens = string.split(" ");
        for (String token : tokens) {
            switch (token) {
                case "o":
                    result.add(4);
                    break;
                case "o|":
                    result.add(2);
                    break;
                case ".|":
                    result.add(1);
                    break;
                default:
                    throw new RuntimeException("Invalid token: " + token);
            }
        }
        return result;
    }
}

