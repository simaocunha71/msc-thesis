        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < game.size(); i++) {
            int diff = Math.abs(guess.get(i) - game.get(i));
            result.add(diff);
        }
        return result;
    }
}

