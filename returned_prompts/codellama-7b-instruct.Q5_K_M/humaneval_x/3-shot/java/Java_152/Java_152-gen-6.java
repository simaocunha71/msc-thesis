        if (game.size() != guess.size())
            throw new IllegalArgumentException("Input arrays must be of equal length.");

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < game.size(); i++) {
            if (game.get(i) == guess.get(i))
                result.add(0);
            else
                result.add(Math.abs(guess.get(i) - game.get(i)));
        }
        return result;
    }
}

