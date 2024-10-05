        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < game.size(); i++) {
            result.add(Math.abs(game.get(i) - guess.get(i)));
        }
        return result;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(s.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(s.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(s.truncateNumber(3.5));
        System.out.println(s.compare(Arrays.asList(1,2,3,4,5,1),Arrays.asList(1,2,3,4,2,-2)));
        System.out.println(s.compare(Arrays.asList(0,5,0,0,0,4),Arrays.asList(4,1,1,0,0,-2)));
    }
}
```