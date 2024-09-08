def dog_age(human_years):
    if human_years <= 2:
        return human_years * 10.5
    else:
        return 21 + (human_years - 2) * 4

print(dog_age(12)) # 61.0

assert dog_age(12)==61
<jupyter_output>
61.0
<jupyter_text>
Question 2
<jupyter_code>
