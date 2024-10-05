        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < game.size(); i++) {
            int difference = Math.abs(game.get(i) - guess.get(i));
            result.add(difference);
        }
        return result;
    }
}