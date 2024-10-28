        return game.stream()
                .map(g -> g - guess.get(game.indexOf(g)))
                .collect(Collectors.toList());
    }
}
