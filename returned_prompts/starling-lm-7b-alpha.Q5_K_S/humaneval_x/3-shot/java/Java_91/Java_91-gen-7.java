        int result = 0;
        boolean current_bored = false;
        for (String word : S.split(" ")) {
            if (word.equals("I")) {
                if (current_bored) result += 1;
                current_bored = true;
            } else {
                current_bored = false;
            }
        }
        return result;
    }
}

