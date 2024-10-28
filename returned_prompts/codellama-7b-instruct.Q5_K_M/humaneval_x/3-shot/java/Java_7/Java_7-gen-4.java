        return strings.stream().filter(string -> string.contains(substring)).collect(Collectors.toList());
    }
}

