        return numbers.stream().filter(i -> numbers.indexOf(i) == numbers.lastIndexOf(i)).collect(Collectors.toList());
    }
}

