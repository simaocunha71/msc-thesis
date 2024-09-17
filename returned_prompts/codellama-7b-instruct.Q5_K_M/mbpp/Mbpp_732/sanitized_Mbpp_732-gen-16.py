def replace_specialchar(sentence:str)->str:
  return sentence.replace(' ','::').replace(',','::').replace('.','::')