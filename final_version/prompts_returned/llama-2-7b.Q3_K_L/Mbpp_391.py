"""
Write a function to convert more than one list to nested dictionary.
assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
"""
from typing import List, Dict
def convert_list_dictionary(list1: List[str], list2:List[str], list3:List[float]) -> Dict[List[str],Dict[str, float]]:
    """
    Convert a list of string to nested dictionary. 
    1) Create an empty Dictionary as result dict.  
    2) For each element in the first list, create an entry in Dictionary as S_name and then fill that with the corresponding elements of list3.
    3) For each element in the second list, create an entry in the nested dictionary inside the previous entry created for S001. Then fill that with the corresponding elements of list2.
    """
    resultDict = {}
    convert_nested_dictionary(list1[0],resultDict,list3)

def convert_nested_dictionary(name: str,dict: Dict[str,float],list_to_fill : List[float]) -> None:
  """
     Add an entry in the nested dictionary and fill that with values of list to be added as key.
    Inputs: name - string for S001 or S002 or.....,  dict - Dictionary created as resultDict,list_to_fill - contains the values corresponding to particular key to add it in the nested dictionary.
    """  
  if name not in dict:
     dict[name] = {}
  convert_nested_dictionary(name+'_'+str(index),dict[name],list_to_fill)

main()
