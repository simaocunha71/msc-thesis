    public String sortNumbers(String numbers) {
        String[] parts = numbers.split(" ");
        Arrays.sort(parts);
        return String.join(" ", parts);
    }
}
