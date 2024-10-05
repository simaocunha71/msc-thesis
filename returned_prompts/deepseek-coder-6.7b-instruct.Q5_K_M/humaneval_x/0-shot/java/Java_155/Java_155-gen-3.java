        List<Integer> result = new ArrayList<>();
        result.add(0);
        result.add(0);
        String numStr = Integer.toString(Math.abs(num));
        for(char c : numStr.toCharArray()){
            if(Integer.parseInt(String.valueOf(c)) % 2 == 0){
                result.set(0, result.get(0) + 1);
            }else{
                result.set(1, result.get(1) + 1);
            }
        }
        return result;
    }
}

*/

