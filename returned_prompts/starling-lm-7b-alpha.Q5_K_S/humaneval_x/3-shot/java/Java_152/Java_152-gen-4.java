        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < game.size(); i++) {
            int actual = game.get(i);
            int guess_value = guess.get(i);
            result.add(Math.abs(actual - guess_value));
        }
        return result;
    }
}



```