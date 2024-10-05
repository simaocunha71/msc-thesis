        String[] words = S.split(" ");
        int result = 0;
        for (String word : words) {
            if (word.equals("I")) result += 1;
            if (word.length() > 0 && (word.charAt(word.length() - 1) == '.' || word.charAt(word.length() - 1) == '!' || word.charAt(word.length() - 1) == '?')) result += 1;
        }
        return result;
    }
}



```