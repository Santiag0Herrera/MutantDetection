def validateInput(matrix):
  if matrix == None:
    return False, "No matrix recived."
  if len(matrix) == 0:
    return False, "Matrix should not be empty."
  if len(matrix) != len(matrix[0]):
    return False, "Matrix should be square (NxN)."
  if len(matrix) < 4 or len(matrix[0]) < 4:
    return False, "Matrix not large enough."
  for string in matrix:
    value, invalidLetter = verifyString(string.upper())
    if not value:
      return False, f"Invalid caracter {invalidLetter}, in DNA sequence :("
  return True, ""

def verifyString(string):
  acceptedLetters = ["A", "T", "C", "G"]
  for letter in string:
    if letter not in acceptedLetters:
      return False, letter
  return True, "-"

def verifyConsecutiveLettersInRow(matrix):
  for wordIndex in range(len(matrix)):
    word = matrix[wordIndex]
    for letterIndex in range(len(word) - 3):
      if word[letterIndex] == word[letterIndex+1] == word[letterIndex+2] == word[letterIndex+3]:
        return True, wordIndex+1
  return False, None

def verifyConsecutiveLettersInColumn(matrix):
  for letterIndex in range(len(matrix[0])):
    for wordIndex in range(len(matrix) - 3):
      if matrix[wordIndex][letterIndex] == matrix[wordIndex+1][letterIndex] == matrix[wordIndex+2][letterIndex] == matrix[wordIndex+3][letterIndex]:
        return True, letterIndex+1
  return False, None

def verifyConsecutiveLettersInDiagonal(matrix):
  for wordIndex in range(len(matrix)-3):
    for letterIndex in range(len(matrix[0])-3):
      if (matrix[wordIndex][letterIndex] == matrix[wordIndex + 1][letterIndex + 1] == matrix[wordIndex + 2][letterIndex + 2] == matrix[wordIndex + 3][letterIndex + 3]):
        return True, f"({wordIndex+1}:{letterIndex+1}) - ({wordIndex+4}:{letterIndex+4})"
  return False, None

def matrixToUpper(matrix):
  for i in range(len(matrix)):
    matrix[i] = matrix[i].upper()