        return values.stream().filter(Integer.class::isInstance).map(Integer.class::cast).collect(Collectors.toList());
    }
}

