        Optional<Integer> minOpt = Optional.empty();
        for (int num : lst) {
            if (minOpt.isPresent() && num < minOpt.get()) {
                return Optional.of(num);
            } else if (!minOpt.isPresent() || num < minOpt.get()) {
                minOpt = Optional.of(num);
            }
        }
        return minOpt.isPresent() ? Optional.empty() : minOpt;
    }
}

