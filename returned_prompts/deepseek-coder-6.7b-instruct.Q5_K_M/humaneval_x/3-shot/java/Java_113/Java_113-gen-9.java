        List<String> result = new ArrayList<>();
        for(int i=0; i<lst.size(); i++){
            String curr = lst.get(i);
            int count = 0;
            for(char c : curr.toCharArray()){
                if((c - '0') % 2 != 0) count++;
            }
            result.add("the number of odd elements " + count + "n the str" + count + "ng " + count + " of the " + count + "nput.");
        }
        return result;
    }
}

