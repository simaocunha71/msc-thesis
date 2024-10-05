        return String.join(" ", LongStream.iterate(0, i -> i + 1).limit(n + 1).mapToObj(String::valueOf).collect(Collectors.toList()));
    }
}

