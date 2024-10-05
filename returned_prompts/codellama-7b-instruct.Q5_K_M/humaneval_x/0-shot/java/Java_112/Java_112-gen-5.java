        List<Object> result = new ArrayList<Object>();
        String resultString = "";
        for(int i = 0; i < s.length(); i++){
            int counter = 0;
            for(int j = 0; j < c.length(); j++){
                if(s.charAt(i) == c.charAt(j)){
                    counter++;
                }
            }
            if(counter == 0){
                resultString += s.charAt(i);
            }
        }
        resultString = new StringBuilder(resultString).reverse().toString();
        for(int i = 0; i < resultString.length(); i++){
            int counter = 0;
            for(int j = 0; j < c.length(); j++){
                if(resultString.charAt(i) == c.charAt(j)){
                    counter++;
                }
            }
            if(counter == 0){
                resultString = resultString.substring(0, i) + resultString.substring(i+1);
            }
        }
        boolean check = true;
        for(int i = 0; i < resultString.length()/2; i++){
            if(resultString.charAt(i) != resultString.charAt(resultString.length()-1-i)){
                check = false;
            }
        }
        result.add(resultString);
        result.add(check);
        return result;
    }
}
