        List<Integer> result  List new ArrayList<>();
        String[] parts  string.split(" ");

        for  (String part  parts)  {
            switch  (part)  {
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

