from validations import verifyConsecutiveLettersInRow, verifyConsecutiveLettersInColumn, verifyConsecutiveLettersInDiagonal

def is_mutant(dna):
  result = False
  detailedResult = {}
  rowValidation, consecutiveRow = verifyConsecutiveLettersInRow(dna)
  columnValidation, consecutiveColumn = verifyConsecutiveLettersInColumn(dna)
  diagonalValidation, consecutiveDiagnoalCoordenates = verifyConsecutiveLettersInDiagonal(dna) 
  result = rowValidation or columnValidation or diagonalValidation
  detailedResult = {
    "isMutant": rowValidation or columnValidation or diagonalValidation,
    "dnaAnalysis": {
      "row": {
        "position": consecutiveRow
      } if rowValidation else None,
      "column": {
        "position": consecutiveColumn
      } if columnValidation else None,
      "diagonal": {
        "position": consecutiveDiagnoalCoordenates
      } if diagonalValidation else None
    }
  }

  return result, detailedResult