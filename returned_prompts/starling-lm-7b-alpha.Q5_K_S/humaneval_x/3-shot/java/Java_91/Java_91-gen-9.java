        int result = 0;
        boolean isBored = false;
        for (String word : S.split(" ")) {
            if (word.equals("I")) {
                if (isBored) result += 1;
                isBored = true;
            } else {
                isBored = false;
            }
        }
        return result;
    }
}

