"""
def max_run_uppercase(s):
    max_run = 0
    run = 0
    for c in s:
        if c.isupper():
            run += 1
        else:
            run = 0
        max_run = max(max_run, run)
    return max_run

def test_max_run_uppercase():
    assert max_run_uppercase('GeMKSForGERksISBESt') == 5

if __name__ == '__main__':
    test_max_run_uppercase()
"""

def max_run_uppercase(s):
    max_run = 0
    run = 0
    for c in s:
        if c.isupper():
            run += 1
        else:
            run = 0
        max_run = max(max_run, run)
    return max_run

print(max_run_uppercase('GeMKSForGERksISBESt')) #5
print(max_run_uppercase('GEMKSForGERksISBEST')) #3
print(max_run_uppercase('GEMKForGERksISBEST')) #2
print(max_run_uppercase('GEMKSForGERkISBEST')) #2
print(max_run_uppercase('GEMKSForGERksISBES')) #4
print(max_run_uppercase('GEMKSForGERksISBESt')) #5
print(max_run_uppercase('GEMKSForGERksISBESTt')) #3
print(max_run_uppercase('GEMKSForGERksISBESTt')) #3
print(max_run_uppercase('GEMKSForGERksISBESTtt')) #3
print(max_run_uppercase('GEMKSForGERksISBESTtt')) #3
print(max_run_uppercase('GEMKSForGERksISBESTttt')) #3
print(max_run_uppercase('GEMKSForGERksISBESTttt')) #3
print(max_run_uppercase('GEMKSForGERksISBESTtttt')) #3
