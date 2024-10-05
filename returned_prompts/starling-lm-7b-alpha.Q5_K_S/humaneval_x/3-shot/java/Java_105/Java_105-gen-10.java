        Collections.sort(arr);
        Collections.reverse(arr);
        List<String> result = new ArrayList<>();

        for (int i = 0; i < arr.size(); i++) {
            switch (arr.get(i)) {
                case 1: result.add("One"); break;
                case 2: result.add("Two"); break;
                case 3: result.add("Three"); break;
                case 4: result.add("Four"); break;
                case 5: result.add("Five"); break;
                case 6: result.add("Six"); break;
                case 7: result.add("Seven"); break;
                case 8: result.add("Eight"); break;
                case 9: result.add("Nine"); break;
                default: result.add(""); break;
            }
        }
        return result;
    }
}

