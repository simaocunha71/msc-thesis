        return strings.stream().filter(str -> str.startsWith(prefix)).collect(Collectors.toList());
    }
}
