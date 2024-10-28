        Set<Integer> values = new HashSet<>();
        List<Integer> result = new ArrayList<>();
        int x = 0, y = 0;
        while (k > 0) {
            result.add(grid.get(x).get(y));
            int next_x = x == 0 ? x : (x - 1);
            int next_y = y == 0 ? y : (y - 1);
            k -= 1;
            while (!values.contains(grid.get(next_x).get(next_y))) {
                values.add(grid.get(next_x).get(next_y));
                next_x = next_x == 0 ? next_x : (next_x - 1);
                next_y = next_y == 0 ? next_y : (next_y - 1);
            }
            values.clear();
            if (next_x < 0 || next_y < 0) {
                x = 0;
                y = (y + 1) % grid.get(0).size();
            } else {
                x = next_x;
                y = next_y;
            }
        }
        return result;
    }
}

