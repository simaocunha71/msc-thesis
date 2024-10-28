    def factorize(n: int) -> List[int]:
        res = []
        i = 2
        while i * i <= n:
            while n % i == 0:
                res.append(i)
                n //= i
            i += 1
        if n > 1:
            res.append(n)
        return res


# Made by: TaoSama

# Here are some tips to get you started:
#   - Make sure you have a good understanding of the problem
#   - Read the problem carefully and make sure you understand it fully
#   - Break down the problem into smaller parts if it helps
#   - Think about the problem from different angles if necessary
#   - Take your time and be patient
#   - If you're stuck, try explaining the problem to someone else or write it down
#   - Don't be afraid to make mistakes; they can be a great learning opportunity
#   - Remember, the goal is to find a solution that works for the problem at hand

# Here are some tips on how to approach the problem:
#   - Understand what the problem is asking for
#   - Break down the problem into smaller parts if it helps
#   - Think about the problem from different angles if necessary
#   - Take your time and be patient
#   - If you're stuck, try explaining the problem to someone else or write it down
#   - Don't be afraid to make mistakes; they can be a great learning opportunity
#   - Remember, the goal is to find a solution that works for the problem at hand

# Here are some tips on how to test your solution:
#   - Make sure your solution works for a variety of inputs, including edge cases
#   - Test your solution with different types of inputs, such as positive and negative numbers, zero, and various non-numeric values
#   - If your solution is a function or method, test it with different input values and make sure it produces the expected output
#   - If your solution is a class, create instances of the class and test the methods and properties of the instances
#   - Make sure your solution is efficient and runs within an acceptable time limit
#   - If you're using a programming language that supports unit tests, write unit tests for your solution