
def anti_shuffle(s):
    words = s.split(' ')
    result = []
    for word in words:
        new_word = ''.join(sorted(word))
        result.append(new_word)
    return ' '.join(result)

print(anti_shuffle('Hi'))  # 'Hi'
print(anti_shuffle('hello'))  # 'ehllo'
print(anti_shuffle('Hello World!!!'))  # 'Hello !!!Wdlor'

# Test case
print(anti_shuffle('take me to semynak'))  # 'aekm e t o keyanms'

# Test case
print(anti_shuffle(''))  # ''

# Test case
print(anti_shuffle('i am a sentence'))  # 'aai m eccnnes'

# Test case
print(anti_shuffle('i'))  # 'i'

# Test case
print(anti_shuffle('i am a sentence!!!'))  # 'aai m eccnnes!!!'

# Test case
print(anti_shuffle('i am a sentence!!! Do you like it?'))  # 'aai m eccnnes!!! Do ou yelik it?'

# Test case
print(anti_shuffle('i am a sentence!!! Do you like it? Capture the flag!'))  # 'aai m eccnnes!!! Do ou yelik it? Cepatuhe fgalk!'

# Test case
print(anti_shuffle('i am a sentence!!! Do you like it? Capture the flag, guess what?!'))  # 'aai m eccnnes!!! Do ou yelik it? Cepatuhe fgalk, eghs wat?!'

# Test case
print(anti_shuffle('i am a sentence!!! Do you like it? Capture the flag, guess what?! I am the best!!!'))  # 'aai m eccnnes!!! Do ou yelik it? Cepatuhe fgalk, eghs wat? I am thebest!!!'

# Test case
print(anti_shuffle('i am a sentence!!! Do you like it?