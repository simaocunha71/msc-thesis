
    binary = bin(decimal).replace("0b","")
    return 'db'+binary+'db'

print(decimal_to_binary(15)) # returns “db1111db”
print(decimal_to_binary(32)) # returns “db100000db”
print(decimal_to_binary(255)) # returns “db1111111db”
print(decimal_to_binary(0)) # returns “db0db”
<jupyter_output>
db1111db
db100000db
db1111111db
db0db
<jupyter_text>
Question 3:
<jupyter_code>
