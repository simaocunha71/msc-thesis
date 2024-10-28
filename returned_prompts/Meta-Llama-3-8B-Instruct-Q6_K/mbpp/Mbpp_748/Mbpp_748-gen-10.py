def capital_words_spaces(s):
    result = ''
    for i in range(len(s)):
        if i > 0 and s[i-1].isupper():
            result += ' '
        result += s[i]
    return result

# Test the function
print(capital_words_spaces("Python"))  # Expected output: 'Python'  # No spaces are needed because all letters are lowercase. 
print(capital_words_spaces("HelloWorld"))  # Expected output: 'Hello World'
print(capital_words_spaces("ThisIsAPythonProgram"))  # Expected output: 'This Is A Python Program'
print(capital_words_spaces("IamLearningPython"))  # Expected output: 'I am Learning Python' 
print(capital_words_spaces("PythonProgramming"))  # Expected output: 'Python Programming'  # No spaces are needed because all letters are lowercase. 
print(capital_words_spaces("PythonIsFun"))  # Expected output: 'Python Is Fun' 
print(capital_words_spaces("PythonIsNotJustForWebDevelopment"))  # Expected output: 'Python Is Not Just For Web Development' 
print(capital_words_spaces("PythonIsNotJustForWebDevelopmentAndDataScience"))  # Expected output: 'Python Is Not Just For Web Development And Data Science' 
print(capital_words_spaces("PythonIsNotJustForWebDevelopmentAndDataScienceAndMachineLearning"))  # Expected output: 'Python Is Not Just For Web Development And Data Science And Machine Learning' 
print(capital_words_spaces("PythonIsNotJustForWebDevelopmentAndDataScienceAndMachineLearningAndArtificialIntelligence"))  # Expected output: 'Python Is Not Just For Web Development And Data Science And Machine Learning And Artificial Intelligence' 
print(capital_words_spaces("PythonIsNotJustForWebDevelopmentAndDataScienceAndMachineLearningAndArtificialIntelligenceAndDeepLearning"))  # Expected output: 'Python Is Not Just For Web Development And Data Science And Machine Learning And Artificial Intelligence And Deep Learning' 
print(capital_words_spaces("PythonIsNotJustForWebDevelopmentAndDataScienceAndMachineLearningAndArtificialIntelligenceAndDeepLearningAndNaturalLanguageProcessing"))  # Expected output: 'Python Is Not Just For Web Development And Data Science And Machine Learning And Artificial Intelligence And Deep Learning And Natural Language Processing' 
print(capital_words_spaces("PythonIsNotJustForWebDevelopmentAndDataScienceAndMachineLearningAndArtificialIntelligenceAndDeepLearningAndNaturalLanguageProcessingAndComputerVision"))  # Expected output: '