    public Map<String, Integer> histogram(String test) {
        Map<String, Integer> result = new HashMap<>();
        String[] words = test.split(" ");
        int maxCount = 0;
        for (String word : words) {
            if (!result.containsKey(word)) {
                result.put(word, 1);
            } else {
                result.put(word, result.get(word) + 1);
            }
            if (result.get(word) > maxCount) {
                maxCount = result.get(word);
            }
        }
        Map<String, Integer> maxCountMap = new HashMap<>();
        for (Map.Entry<String, Integer> entry : result.entrySet()) {
            if (entry.getValue() == maxCount) {
                maxCountMap.put(entry.getKey(), entry.getValue());
            }
        }
        return maxCountMap;
    } 














    }

    } 














    } 





    } 














    } 





    } 














    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 





    } 














    } 