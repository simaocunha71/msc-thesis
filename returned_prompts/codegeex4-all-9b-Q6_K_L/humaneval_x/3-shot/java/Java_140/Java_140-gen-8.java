        String[] words = text.split(" ");
        StringBuilder result = new StringBuilder();
        for (String word : words) {
            if (word.length() > 0) {
                result.append(word);
                result.append("_");
            }
        }
        return result.toString().replaceAll("_+", "-").replaceAll("_$", "");

    }
}

