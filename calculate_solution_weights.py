molecular_weights = {
    'NaCl': 58.44,
    'H2SO4': 98.079,
    'NaOH': 40.00,
    'KMnO4': 158.034,
    'CH3COOH': 60.052
}

solutions_needed = ['NaCl-0.5M', 'H2SO4-0.25M', 'NaOH-1M', 'KCl-0.1M', 'CH3COOH-0.3M']

def calculate_solution_weights(molecular_weights, solutions_needed):
    # First we need to make sure to go through all of the components of the list solutions_needed:
    for i in range(len(solutions_needed)):
        # Then we need to check if that chemical is also included in the dictionary molecular_weights:
        if solutions_needed[i].split('-')[0] in molecular_weights:
            chemical = solutions_needed[i].split('-')[0] # This is just to make things easier when writing out the new value for that index in the list
            concentration = float(solutions_needed[i].split('-')[1][:-1]) # Getting the numerical value of the concentration
            weight = molecular_weights.get(chemical) * concentration # Using the given equation to calculate the weight of the chemical
            solutions_needed[i] = f'{chemical}-{concentration}M-{weight}g' # String output formatted as requested
        else:
            solutions_needed[i] = 'unknown' # This is to keep the requirement that if the chemical isn't found in molecular_weights, the function should return 'unknown'
    # Return statement to show what the function did to the list:
    return solutions_needed

if __name__ == "__main__":
    result = calculate_solution_weights(molecular_weights, solutions_needed)
    print(result)
