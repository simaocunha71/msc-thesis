    public String sortNumbers(String numbers) {
        String[] words = numbers.split(" ");
        Arrays.sort(words);
        return String.join(" ", words);
    }  



