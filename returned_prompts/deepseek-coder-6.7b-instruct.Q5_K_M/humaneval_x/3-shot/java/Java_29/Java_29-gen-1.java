        return strings.stream()
            .filter(string -> string.startsWith(prefix))
            .collect(Collectors.toList());
     }
}

