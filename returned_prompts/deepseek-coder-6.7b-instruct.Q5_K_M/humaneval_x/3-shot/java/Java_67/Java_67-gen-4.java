        String[] splitString = s.split(" ");
        int apples = Integer.parseInt(splitString[0]);
        int oranges = Integer.parseInt(splitString[2]);
        return n - apples - oranges;
     }
}

