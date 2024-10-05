        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < game.size(); i++) {
            result.add(Math.abs(guess.get(i) - game.get(i)));
        }
        return result;
    }
}