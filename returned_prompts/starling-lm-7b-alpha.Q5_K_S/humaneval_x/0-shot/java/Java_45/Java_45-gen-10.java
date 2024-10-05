        return (a*h)/2.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int h = sc.nextInt();
        Solution s = new Solution();
        System.out.println(s.triangleArea(a,h));
    }
}







```