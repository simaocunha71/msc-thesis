        return String.join(" ", IntStream.range(0, n + 1).mapToObj(i -> Integer.toString(i)).collect(Collectors.toList()));
    }
}

