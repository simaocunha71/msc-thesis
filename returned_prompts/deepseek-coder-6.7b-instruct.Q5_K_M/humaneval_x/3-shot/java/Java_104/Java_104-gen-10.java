        List<Integer> result = new ArrayList<>();
        for(Integer num : x){
            if(num.toString().matches("[02468]")){
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }
}

