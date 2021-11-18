from alphabet import alphabet, tebahpla

class VigenereCypher:
  def __init__ (self, key: str):
    self.key = key.lower()

  def encryptChar (self, char: str, position: str):
    try:
      # Get the value of the character, then add the value of the character at key[position] and turn it back into a character
      return tebahpla[(alphabet[char.lower()] + alphabet[self.key[position % len(self.key)]]) % len(alphabet)]
    except KeyError:
      # If the character is not aphanumeric, then don't change it
      return char

  def encryptString (self, data: str) -> str:
    '''Encrypt each character in data, then retun that value
    '''
    temp = ""
    for i in range(len(data)):
      temp += self.encryptChar(char=data[i], position=i)
    return temp

  def decryptChar (self, char: str, position: str) -> str:
    try:
      return tebahpla[(alphabet[char.lower()] - alphabet[self.key[position % len(self.key)]]) % len(alphabet)]
    except KeyError:
      return char

  def decryptString (self, data: str) -> str:
    temp = ""
    for i in range(len(data)):
      temp += self.decryptChar(char=data[i], position=i)
    return temp