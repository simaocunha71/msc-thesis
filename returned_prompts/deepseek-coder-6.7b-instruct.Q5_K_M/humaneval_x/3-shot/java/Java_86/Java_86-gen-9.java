        String[] words = s.split(" ");
        StringBuilder result = new StringBuilder();

        for (String word : words) {
            result.append(sortString(word) + " ");
        }

        return result.toString().trim();
    }

    public String sortString(String inputString) {
        // Convert input string to char array
        char tempArray[] = inputString.toCharArray();

        // Sort tempArray
        Arrays.sort(tempArray);

        // Return new sorted string
        return new String(tempArray);
    }
}

