        if (a + b < c || b + c < a || c + a < b) {
            return -1;
        }

        double area = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));

        return area;
    }

    public static void main(String[] args) {
        double a = 3;
        double b = 4;
        double c = 5;

        Solution sol = new Solution();
        double area = sol.triangleArea(a, b, c);

        System.out.println(area);
    }
}
