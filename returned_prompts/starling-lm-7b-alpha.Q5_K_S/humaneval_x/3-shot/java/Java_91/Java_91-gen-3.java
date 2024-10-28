        int result = 0;
        boolean is_boredom = false;
        for (String word : S.split("[.?!]")) {
            if (word.equals("I")) {
                if (!is_boredom) result += 1;
                is_boredom = true;
            } else {
                is_boredom = false;
            }
        }
        return result;
    }
}

