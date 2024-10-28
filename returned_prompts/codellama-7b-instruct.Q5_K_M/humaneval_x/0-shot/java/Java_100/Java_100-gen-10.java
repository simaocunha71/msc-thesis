        List<Integer> levels = new ArrayList<Integer>();
        int nextLevelStones = n;
        while (nextLevelStones > 0) {
            levels.add(nextLevelStones);
            nextLevelStones = (nextLevelStones % 2 == 0) ? nextLevelStones + 1 : nextLevelStones + 2;
        }
        return levels;
    }
}

