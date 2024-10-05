        return strings.stream().reduce((a, b) -> a + b).orElse("");
    }
}

