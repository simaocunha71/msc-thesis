        String[] numArray = numbers.split(" ");
        for (int i = 0; i < numArray.length; i++) {
            for (int j = i + 1; j < numArray.length; j++) {
                if (numArray[i].length() > numArray[j].length()) {
                    String temp = numArray[i];
                    numArray[i] = numArray[j];
                    numArray[j] = temp;
                }
            }
        }
        return String.join(" ", numArray);
    }
}

