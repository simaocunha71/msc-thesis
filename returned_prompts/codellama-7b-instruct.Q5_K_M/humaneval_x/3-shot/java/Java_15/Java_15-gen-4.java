        return String.join(" ", IntStream.rangeClosed(0, n).mapToObj(String::valueOf).collect(Collectors.toList()));
    }
}

