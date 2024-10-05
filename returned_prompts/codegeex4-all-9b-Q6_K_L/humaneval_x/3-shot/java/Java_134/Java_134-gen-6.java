for (int i = 0; i < numbers.size() - 1; i++) {
    for (int j = i + 1; j < numbers.size(); j++) {
        if (Math.abs(numbers.get(i) - numbers.get(j)) < threshold) return true;
    }
}
return false;

