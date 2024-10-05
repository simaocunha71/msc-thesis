        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < game.size(); i++) {
            if (guess.get(i) == game.get(i)) {
                result.add(0);
            } else {
                result.add(Math.abs(guess.get(i) - game.get(i)));
            }
        }
        return result;
    }
}

