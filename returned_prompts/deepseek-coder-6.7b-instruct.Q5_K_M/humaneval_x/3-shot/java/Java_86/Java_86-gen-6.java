        String[] words = s.split(" ");
        StringBuilder sb = new StringBuilder();

        for(String word: words){
            sb.append(sortString(word) + " ");
        }

        return sb.toString().trim();
    }

    public static String sortString(String inputString)
    {
        // Convert input string to char array
        char tempArray[] = inputString.toCharArray();

        // Sort tempArray
        Arrays.sort(tempArray);

        // Return new sorted string
        return new String(tempArray);
    }
}

