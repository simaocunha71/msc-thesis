    List<Integer> interspersedNumbers = new ArrayList<Integer>();
    for (int i = 0; i < numbers.size(); i++) {
        interspersedNumbers.add(numbers.get(i));
        if (i < numbers.size() - 1) {
            interspersedNumbers.add(delimiter);
        }
    }
    return interspersedNumbers;
}

}

