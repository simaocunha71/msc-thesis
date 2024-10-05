        List<Integer> result = new ArrayList<>();
        for (String token : string.split("\\|")) {
            if (token.equals("o")) {
                result.add(4);
            } else if (token.equals(".")) {
                result.add(1);
            } else {
                result.add(2);
            }
        }
        return result;
    }
}

