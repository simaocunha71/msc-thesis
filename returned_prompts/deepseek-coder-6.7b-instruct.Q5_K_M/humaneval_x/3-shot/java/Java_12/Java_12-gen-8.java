        return strings.stream()
            .reduce((a, b) -> a.length() > b.length() ? a : b);
     }
}

