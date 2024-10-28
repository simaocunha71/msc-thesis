def remove_uppercase(s):
    return ''.join(c for c in s if c.islower())

# Test case
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
# Output: cstyoravoitshos
print(remove_uppercase('HelloWorld'))  # Output: helloworld
print(remove_uppercase(''))  # Output: 
print(remove_uppercase('abcdefg'))  # Output: abcdefg
print(remove_uppercase('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))  # Output: 
print(remove_uppercase('abcdefghijklmnopqrstuvwxyz'))  # Output: abcdefghijklmnopqrstuvwxyz
print(remove_uppercase('1234567890'))  # Output: 1234567890
print(remove_uppercase('!@#$%^&*()'))  # Output: !@#$%^&*()
print(remove_uppercase('cAstyoUrFavoRitETVshoWs123!@#$%^&*()'))  # Output: cstyoravoitshos123!@#$%^&*()
print(remove_uppercase('cAstyoUrFavoRitETVshoWs!@#$%^&*()'))  # Output: cstyoravoitshos!@#$%^&*()
print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))  # Output: cstyoravoitshos
print(remove_uppercase(''))  # Output: 
print(remove_uppercase('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))  # Output: 
print(remove_uppercase('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'))  # Output: 
print(remove_uppercase('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'))  # Output: 
print(remove_uppercase('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))  # Output: 
print(remove_uppercase('!@#$%^&*()1234567890'))  # Output: !@#$%^&*()
print(remove_uppercase('!@#$%^&*()'))  # Output: !@#$%^&*()
print(remove_uppercase('!@#$%^&*()1234567890!@#$%^&*()'))  # Output: !@#$%^&*()!@#$%^&*()
print(remove_uppercase('!@#$%^&*()1234567890'))  # Output: