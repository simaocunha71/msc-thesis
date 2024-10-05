        double max_strength = 0;
        String strongest_extension = "";
        for (String ext : extensions) {
            double strength = (double) (ext.chars().filter(c -> c >= 'A' && c <= 'Z').count()) -
                    (double) (ext.chars().filter(c -> c >= 'a' && c <= 'z').count());
            if (strength > max_strength) {
                max_strength = strength;
                strongest_extension = ext;
            } else if (strength == max_strength && ext.compareTo(strongest_extension) < 0) {
                strongest_extension = ext;
            }
        }
        return class_name + "." + strongest_extension;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.StrongestExtension("my_class", Arrays.asList("AA", "Be", "CC")));
    }
}
```