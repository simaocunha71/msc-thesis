        boolean increasing = true;
        boolean decreasing = true;

        for (int i = 0; i < l.size() - 1; i++) {
            if (l.get(i) > l.get(i + 1)) {
                increasing = false;
            }
            if (l.get(i) < l.get(i + 1)) {
                decreasing = false;
            }
        }

        return increasing || decreasing;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println(s.monotonic(Arrays.asList(1, 2, 4, 20))); // true
        System.out.println(s.monotonic(Arrays.asList(1, 20, 4, 10))); // false
        System.out.println(s.monotonic(Arrays.asList(4, 1, 0, -10))); // true
    }
}

'''

print(solution(problem))
'''

# Output:
'''
True
False
True
'''

# Explanation:
'''
The first example [1, 2, 4, 20] is a monotonically increasing sequence.
The second example [1, 20, 4, 10] is not monotonically increasing or decreasing.
The third example [4, 1, 0, -10] is a monotonically increasing sequence.
'''

# Solution:
'''
The solution is to iterate through the list and check if the sequence is either increasing or decreasing. If it is, return True. If not, return False.
'''

# Complexity:
'''
The time complexity is O(n) as we are iterating through the list once. The space complexity is O(1) as we are using a constant amount of space.
'''
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2: Given a string s and an integer k, return the length of the longest substring that contains at most k