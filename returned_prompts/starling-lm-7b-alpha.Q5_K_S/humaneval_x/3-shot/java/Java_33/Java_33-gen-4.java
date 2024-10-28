        List<Integer> result = new ArrayList<>();
        result.addAll(l.subList(0, l.size() % 3));
        result.addAll(l.subList(l.size() % 3, l.size()).stream().sorted().collect(Collectors.toList()));
        return result;
    }
}

