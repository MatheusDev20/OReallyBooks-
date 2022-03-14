from hashlib import new


new_dict = {"A": '1', 'B': '2', 'C': '3'}
print('A' in new_dict) # Underneath call me dunder method __contains__
# print(new_dict.clear()) # Remove all dict items


shallow_copy = new_dict.copy()
shallow_copy['A'] = '3'

old_list = [1,2,3]
new_list = old_list # passa a referência da old_list para a new_list, qualquer valor alterado na new_list
                    # also altera a old_list também

new_list[0] = 2 # Alterar a old e new lists
print(old_list) # [2,2,3]
print(new_list) # [2,2,3]

