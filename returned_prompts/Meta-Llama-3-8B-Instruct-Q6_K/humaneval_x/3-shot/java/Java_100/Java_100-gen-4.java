        List<Integer> result = new ArrayList<>();
        int current_level = n;

        while (current_level > 0) {
            result.add(0, current_level);
            current_level = (current_level % 2 == 0) ? current_level + 1 : current_level - 1;
        }
        return result;
    }
}

