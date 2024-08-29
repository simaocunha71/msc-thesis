def count_reverse_pairs(lst):
    count = 0
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] == lst[j][::-1]:
                count += 1
    return count

print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])) # 2

# Answer: 2
# Explanation: The pairs of reverse strings are ("julia", "ailuj") and ("best", "tseb")
<jupyter_output>
2
<jupyter_text>
