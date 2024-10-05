        int[] arr = new int[n];
        for(int i = 0; i<n; i++) {
            arr[i] = (i+1)*(i+1) - (i+1) + 1;
        }
        int count = 0;
        for(int i = 0; i<n; i++) {
            for(int j = i+1; j<n; j++) {
                for(int k = j+1; k<n; k++) {
                    if(arr[i] + arr[j] + arr[k] % 3 == 0) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(solution.getMaxTriples(n));
    }
}














```