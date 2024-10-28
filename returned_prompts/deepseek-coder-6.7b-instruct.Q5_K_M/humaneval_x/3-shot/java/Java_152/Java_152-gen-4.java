        List<Integer> result = new ArrayList<>();

        for  (int i = 0; i < game.size(); i++) {
            result.add(Math.abs(game.get(i) - guess.get(i)));
        }
        return result;
     }
}

