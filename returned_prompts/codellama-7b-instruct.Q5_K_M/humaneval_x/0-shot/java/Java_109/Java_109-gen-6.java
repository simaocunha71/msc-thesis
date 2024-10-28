        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) < arr.get(i - 1)) {
                arr.remove(i);
                arr.add(0, arr.get(i));
                i--;
                continue A;
            }
        }
        return arr.stream().sorted().collect(Collectors.toList()).equals(arr);
    }
}

