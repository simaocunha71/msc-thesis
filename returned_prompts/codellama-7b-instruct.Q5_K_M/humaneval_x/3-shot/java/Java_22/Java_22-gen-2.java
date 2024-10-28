        return values.stream().filter(x -> x instanceof Integer).map(x -> (Integer) x).collect(Collectors.toList());
    }
}

