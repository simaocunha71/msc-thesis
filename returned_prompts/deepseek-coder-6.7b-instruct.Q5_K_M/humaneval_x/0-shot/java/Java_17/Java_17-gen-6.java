        List<Integer> list = new ArrayList<>();
        String[] arr = string.split(" ");
        for(String s : arr){
            if(s.equals("o")) list.add(4);
            if(s.equals("o|")) list.add(2);
            if(s.equals(".|")) list.add(1);
        }
        return list;
    }
}

The question is about parsing a string and creating a list based on specific conditions. The solution provided is quite straightforward, it splits the string into an array of strings based on spaces, then based on conditions adds the correct number of beats to the list. It should work as expected for the given conditions.

*/

//Q2:
/*
