        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < game.size(); i++) {
            int diff = Math.abs(game.get(i) - guess.get(i));
            result.add(diff);
        }
        return result;
    }
}

