        List<Integer> result = new ArrayList<>();
        for (String note : string.split(" ")) {
            switch (note) {
                case "o":
                    result.add(4);
                    break;
                case "o|":
                    result.add(2);
                    break;
                case ".|":
                    result.add(1);
                    break;
                default:
                    break;
            }
        }
        return result;
    }
}

