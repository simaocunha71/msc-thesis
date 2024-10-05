        int result = 0;
        boolean in_boredom = false;
        for (String word : S.split("[ .!?]")) {
            if (word.equals("I")) {
                if (!in_boredom) {
                    result += 1;
                    in_boredom = true;
                }
            } else {
                in_boredom = false;
            }
        }
        return result;
    }
}

