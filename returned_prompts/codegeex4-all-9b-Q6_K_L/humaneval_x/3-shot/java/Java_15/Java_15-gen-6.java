        return IntStream.rangeClosed(0, n).mapToObj(i -> String.valueOf(i)).collect(Collectors.joining(" "));
    }
}

