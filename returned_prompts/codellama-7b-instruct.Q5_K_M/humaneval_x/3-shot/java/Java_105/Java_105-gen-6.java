        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) >= 1 && arr.get(i) <= 9) {
                result.add(arr.get(i));
            }
        }
        result.sort(Integer::compareTo);
        Collections.reverse(result);

        List<String> final_result = new ArrayList<>();

        for (int i = 0; i < result.size(); i++) {
            switch (result.get(i)) {
                case 1:
                    final_result.add("One");
                    break;
                case 2:
                    final_result.add("Two");
                    break;
                case 3:
                    final_result.add("Three");
                    break;
                case 4:
                    final_result.add("Four");
                    break;
                case 5:
                    final_result.add("Five");
                    break;
                case 6:
                    final_result.add("Six");
                    break;
                case 7:
                    final_result.add("Seven");
                    break;
                case 8:
                    final_result.add("Eight");
                    break;
                case 9:
                    final_result.add("Nine");
                    break;
                default:
                    final_result.add("");
                    break;
            }
        }
        return final_result;
    }
}

