        return l.stream().max(Comparator.naturalOrder()).orElse(0);
    }
}

