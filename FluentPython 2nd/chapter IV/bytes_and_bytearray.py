# Imuttable type to represent sequence of bytes ( bytes )
# Muttable type to represent sequence of bytes ( bytearray )

cafe = bytes('café', encoding='utf_8')
# retorna 99 o inteiro que mapeia para o caracterce "c" na tabela ASCII
print(type(cafe[0]))
