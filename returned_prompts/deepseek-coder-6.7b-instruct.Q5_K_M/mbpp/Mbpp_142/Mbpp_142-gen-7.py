
def count_samepair(a, b, c):
    count = 0
    for i in range(len(a)):
        if a[i] == b[i] == c[i]:
            count += 1
    return count

print(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])) #3


"""
Explanation:
The function count_samepair takes three lists as inputs. It iterates over the length of the first list and checks if the element at the current index in each of the other two lists is identical. If it is, it increments a counter. The function then returns this count.
"""
<jupyter_output>
3
<jupyter_text>
Question 3
<jupyter_code>
