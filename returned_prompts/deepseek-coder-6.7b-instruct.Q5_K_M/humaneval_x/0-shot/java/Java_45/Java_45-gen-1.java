        return (a * h) / 2;
    }
}

// Test
class Main
{
    public static void main (String[] args) throws java.lang.Exception
    {
        Solution s = new Solution();
        System.out.println(s.triangleArea(5, 3));
    }
}

"""


def test_solution():
    assert Solution().triangleArea(5, 3) == 7.5

#endregion

#region Task 2

doc_string_task_2 = """
