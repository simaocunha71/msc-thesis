        return values.stream().filter(o -> o instanceof Integer).map(o -> (Integer) o).collect(Collectors.toList());
    }
}

