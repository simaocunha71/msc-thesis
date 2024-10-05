        StringBuilder result = new StringBuilder();

        for(char c : text.toCharArray()){
            if(!isVowel(c)) result.append(c);
        }

        return result.toString();
    }

    private boolean isVowel(char c){
        c = Character.toLowerCase(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}

