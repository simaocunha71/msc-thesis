        return l.stream().distinct().sorted().collect(Collectors.toList());
    }
}

