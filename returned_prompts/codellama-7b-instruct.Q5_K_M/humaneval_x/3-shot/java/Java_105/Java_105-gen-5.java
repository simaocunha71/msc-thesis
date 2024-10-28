        List<String> result = new ArrayList<>();

        // sort the array
        arr.sort(Integer::compare);

        // reverse the array
        Collections.reverse(arr);

        // convert each number to its corresponding word
        for (int i = 0; i < arr.size(); i++) {
            int num = arr.get(i);
            if (num >= 1 && num <= 9) {
                String word = "";
                switch (num) {
                    case 1:
                        word = "One";
                        break;
                    case 2:
                        word = "Two";
                        break;
                    case 3:
                        word = "Three";
                        break;
                    case 4:
                        word = "Four";
                        break;
                    case 5:
                        word = "Five";
                        break;
                    case 6:
                        word = "Six";
                        break;
                    case 7:
                        word = "Seven";
                        break;
                    case 8:
                        word = "Eight";
                        break;
                    case 9:
                        word = "Nine";
                        break;
                }
                result.add(word);
            }
        }

        return result;
    }
}

