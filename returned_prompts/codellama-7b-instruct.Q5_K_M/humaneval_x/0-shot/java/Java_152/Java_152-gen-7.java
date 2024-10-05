        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < game.size(); i++) {
            int score = game.get(i);
            int guessed = guess.get(i);
            int difference = Math.abs(score - guessed);
            result.add(difference);
        }
        return result;
    }

}
