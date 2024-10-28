        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < game.size(); i++) {
            if (game.get(i) == guess.get(i)) {
                result.add(0);
            } else {
                result.add(Math.abs(game.get(i) - guess.get(i)));
            }
        }
        return result;
    }
}

