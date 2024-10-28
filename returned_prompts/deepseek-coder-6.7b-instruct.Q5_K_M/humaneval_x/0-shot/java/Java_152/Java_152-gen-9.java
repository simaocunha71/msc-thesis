        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < game.size(); i++) {
            result.add(Math.abs(game.get(i) - guess.get(i)));
        }
        return result;
    }
}

This solution iterates through each element in the input lists (game and guess), calculates the absolute difference between the corresponding elements, and adds this difference to the result list. It returns this result list.

