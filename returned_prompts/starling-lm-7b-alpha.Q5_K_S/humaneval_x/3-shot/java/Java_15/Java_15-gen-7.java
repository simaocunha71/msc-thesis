        return String.join(" ", IntStream.range(0, n + 1).mapToObj(String::valueOf).collect(Collectors.toList()));
    }
}

