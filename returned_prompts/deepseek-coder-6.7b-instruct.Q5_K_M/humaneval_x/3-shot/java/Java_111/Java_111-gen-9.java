        String[] words = test.split(" ");
        Map<String, Integer> map = new HashMap<String, Integer>();

        for(String word : words){
            if(!map.containsKey(word)){
                map.put(word, 1);
            } else {
                map.put(word, map.get(word) + 1);
            }
        }

        int max = 0;
        for(String key : map.keySet()){
            if(map.get(key) > max){
                max = map.get(key);
            }
        }

        Map<String, Integer> result = new HashMap<String, Integer>();
        for(String key : map.keySet()){
            if(map.get(key) == max){
                result.put(key, max);
            }
        }

        return result;
    }
}

