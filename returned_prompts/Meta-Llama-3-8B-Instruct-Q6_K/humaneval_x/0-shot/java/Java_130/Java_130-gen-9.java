    public List<Integer> tri(int n) {
        List<Integer> result = new ArrayList<>();
        result.add(3); // tri(1) = 3
        int evenTri = 1; // tri(2) = 1 + (2 / 2) = 2
        int oddTri = 3; // tri(3) = tri(2) + tri(1) + tri(4) = 2 + 3 + 3 = 8

        for (int i = 2; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(evenTri);
                evenTri = (int) ((evenTri + 1) / 2.0); // tri(n) = 1 + n / 2, if n is even.
            } else {
                result.add(oddTri);
                int temp = oddTri;
                oddTri = result.get(i - 2) + result.get(i - 1) + evenTri; // tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
                evenTri = temp;
            }
        }
        return result;
    }
}
// Time complexity: O(n)
// Space complexity: O(n) for the result list.  // 4ms, 67.3 MB
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
