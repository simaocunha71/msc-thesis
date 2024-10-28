        List<Integer> result = new ArrayList<>();
        if(game.size() != guess.size())
        {
            throw new IllegalArgumentException("The game and guess arrays must be of the same size");
        }
        for(int i = 0; i < game.size(); i++)
        {
            if(guess.get(i) == 0)
            {
                result.add(0);
            }
            else
            {
                result.add(Math.abs(guess.get(i) - game.get(i)));
            }
        }
        return result;
    }

}