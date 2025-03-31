import re

def main(file):

    # Parse the chemical file and extract unique species and reactions
    # The file should be in the same directory as this script
    uniqueSpecies, reactions = parseChemFile(file)

    # Print the unique species and reactions
    print('Unique Species:')
    for species in uniqueSpecies:
        print(species)
    print('\nReactions:')
    for reaction in reactions:
        print(f"R{reactions.index(reaction)+1}: {reaction['description']}")

    # Print details of a particular reaction as an example
    print('\nDetails of Reaction 1:')
    reaction = reactions[0]
    reactionDescription = reaction['description']
    lhsSpecies = reaction['lhsSpecies']
    lhsStoichiometricCoeffs = reaction['lhsStoichiometricCoeffs']
    rhsSpecies = reaction['rhsSpecies']
    rhsStoichiometricCoeffs = reaction['rhsStoichiometricCoeffs']
    backwardReaction = reaction['backwardReaction']
    print(f"Description: {reactionDescription}")
    for idx in range(len(lhsSpecies)):
        print(f"Reactant (Left Hand Side): {lhsStoichiometricCoeffs[idx]} {lhsSpecies[idx]}")
    for idx in range(len(rhsSpecies)):
        print(f"Product (Right Hand Side): {rhsStoichiometricCoeffs[idx]} {rhsSpecies[idx]}")
    print(f"Backward Reaction: {backwardReaction}")
    
    # Return 0 if the script runs successfully
    return 0

def parseChemFile(file):
    """
    Parse a chemical file and extract relevant information.
    """
    # Read the file and remove commented and empty lines
    with open(file, 'r') as f:
        lines = f.readlines()

    # Analyze every line and extract relevant information
    uniqueSpecies = []
    reactions = []
    for line in lines:
        cleanLine = line.strip()
        # Skip empty lines and comment lines
        if not cleanLine or cleanLine.startswith('%'):
            continue
        # Parse reaction information
        reaction = parseReactionStr(cleanLine.split('|')[0].strip())
        if reaction not in reactions:
            reactions.append(reaction)
        # Extract species present in the reaction and add to the list
        for species in reaction['lhsSpecies']:
            if species not in uniqueSpecies:
                uniqueSpecies.append(species)
        for species in reaction['rhsSpecies']:
            if species not in uniqueSpecies:
                uniqueSpecies.append(species)

    # Return the list of unique species and reactions
    return uniqueSpecies, reactions

def parseReactionStr(reactionStr):
    """
    Parse a reaction string and extract relevant information.
    """
    # Split the reaction string into reactants and products
    if '<->' in reactionStr:
        backwardReaction = True
        lhsStr, rhsStr = reactionStr.split('<->')
    elif '->' in reactionStr:
        backwardReaction = False
        lhsStr, rhsStr = reactionStr.split('->')
    else:
        raise ValueError("Invalid reaction string format")
    
    # Extract species from the left-hand side (reactants)
    lhsSpecies, lhsStoichiometricCoeffs = parseSpeciesStr(lhsStr)
    
    # Extract species from the right-hand side (products)
    rhsSpecies, rhsStoichiometricCoeffs = parseSpeciesStr(rhsStr)
    
    # Create reaction dictionary
    # Para reacción reversible, se concatenan las listas de ambos lados
    if backwardReaction:
        combinedSpecies = lhsSpecies + rhsSpecies
        combinedCoeffs = lhsStoichiometricCoeffs + rhsStoichiometricCoeffs
        reaction = {
            'description': reactionStr,
            'lhsSpecies': combinedSpecies,
            'lhsStoichiometricCoeffs': combinedCoeffs,
            'rhsSpecies': combinedSpecies,
            'rhsStoichiometricCoeffs': combinedCoeffs,
            'backwardReaction': backwardReaction
        }
    else:
        reaction = {
            'description': reactionStr,
            'lhsSpecies': lhsSpecies,
            'lhsStoichiometricCoeffs': lhsStoichiometricCoeffs,
            'rhsSpecies': rhsSpecies,
            'rhsStoichiometricCoeffs': rhsStoichiometricCoeffs,
            'backwardReaction': backwardReaction
        }
    return reaction

def parseSpeciesStr(str):
    """
    Parse a species string and extract relevant information.
    """
    # Define regular expression to extract species and their stoichiometric coefficients
    speciesPattern = r'(?:^|\s|[+])(\d*)\s*([eE]|[A-Za-z][A-Za-z0-9]*\([^)]*\))(?=\s|[+]|$)'

    # Extract species from the left-hand side (reactants)
    matches = re.findall(speciesPattern, str)
    speciesList = []
    stoichiometricCoeffList = []
    for match in matches:
        coeff = int(match[0]) if match[0] else 1  # Default coefficient is 1
        species = match[1].strip()
        if species not in speciesList:
            speciesList.append(species)
            stoichiometricCoeffList.append(coeff)
        else:
            index = speciesList.index(species)
            stoichiometricCoeffList[index] += coeff

    return speciesList, stoichiometricCoeffList

if __name__ == "__main__":
    main('helium.chem')