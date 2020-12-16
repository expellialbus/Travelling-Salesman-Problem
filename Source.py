from random import randint

def main () :
    path = run ()

    print ("The sortest path is : " , end = '') ;

    for city in range (len (path)) :
        if city == (len (path) - 1) :
            print (path [city])

        else :
            print (path [city] , "---> " , end = '')

def run () :
    cities = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G']
    map = createMap ()
    population = startingPopulation (map , cities)

    previous = list ()
    condition = True

    # The argument of range function is the number of evolution
    # you may change the number of evolution. It's up to you.

    for i in range (1000) :
        best_chromosome = findPurposeValue (map , population)

        # This "if" statement for comparing previous with best chromosome
        # and just execute once.

        if condition :
            previous = [i for i in best_chromosome]
            condition = False

        else :
            if calculateDistance (map , best_chromosome) < calculateDistance (map , previous) :
                previous = [i for i in best_chromosome]

        # At this point the best chromosome has to remove from population.
        # Otherwise it will do crossing over with itself.

        population.remove (best_chromosome)
        population = crossingOver (population , best_chromosome , cities)

        # Finally the best chromosome has to append to the population.
        # Otherwise the population will evanesce approximately at 6 generation.
        # (The iteration of evanesce is changeable according as your number of city)

        population.append (best_chromosome)

    # The previous variable is contain the shortest path (in other words the best chromosome).

    return previous

def createMap () :
    map = dict ()

    # At this point we have to create a map to apply our genetic algorithm.
    # There is 7 city and their ways from each one to other one.
    # You may set up distance according to your problem.

    map ['A'] = {'B' : 3 , 'C' : 7 , 'D' : 12 , 'E' : 9 , 'F' : 4 , 'G' : 15}
    map ['B'] = {'A' : 3 , 'C' : 2 , 'D' : 6 , 'E' : 5 , 'F' : 8 , 'G' : 13}
    map ['C'] = {'A' : 7 , 'B' : 2 , 'D' : 4 , 'E' : 3 , 'F' : 1 , 'G' : 5}
    map ['D'] = {'A' : 12 , 'B' : 6 , 'C' : 4 , 'E' : 11 , 'F' : 9 , 'G' : 5}
    map ['E'] = {'A' : 9 , 'B' : 5 , 'C' : 3 , 'D' : 11 , 'F' : 4 , 'G' : 1}
    map ['F'] = {'A' : 4 , 'B' : 8 , 'C' : 1 , 'D' : 9 , 'E' : 4 , 'G' : 7}
    map ['G'] = {'A' : 15 , 'B' : 13 , 'C' : 5 , 'D' : 5 , 'E' : 1 , 'F' : 7}

    return map

def startingPopulation (map , list_of_cities) :
    population = list ()

    # For 7 cities there is 7! possible population  at the beginning.
    # This means you can select your number of population between 1 and 5,040.

    number_of_population = randint (5 , 10)

    for count in range (number_of_population) :
        chromosome = list ()

        while len (chromosome) < 7 :

            # "randint" method generate a random number
            # between starting parameter (inclusive) and ending parameter (inclusive).
            # So the range has to decrease once.

            random_index = randint (0 , (len (list_of_cities) - 1))

            if list_of_cities [random_index] not in chromosome :
                chromosome.append (list_of_cities [random_index])

        population.append (chromosome)

    return population

def findPurposeValue (map , population) :
    results = dict ()

    for chromosome in population :
        results [calculateDistance (map , chromosome)] = chromosome

    value = min (results)

    return results [value]

def calculateDistance (map , chromosome) :
    distance = 0

    for city in range (len (chromosome) - 1) :
        neighbors = map [chromosome [city]]
        distance += neighbors [chromosome [city + 1]]

    return distance

def crossingOver (population , best_chromosome , cities) :

    # "split pieces" variable is determine the number of gene swap for crossing over

    split_pieces = randint (1 , (len (population [0]) // 2))

    i = 0

    while i < len (population) :
        j = -1

        while j >= (-1 * split_pieces) :
            population [i][j] = best_chromosome [j]
            j -= 1

        population [i] = checkDuplicates (population [i] , cities)

        # After the crossing over, there may be a mutation.
        # This means the realize condition have to be randomly to mutation.
        # And the solution is the "randint" method again.

        if randint (1 , 15) % 3 == 0 :
            population [i] = mutation (population [i])

        i += 1

    return population

def checkDuplicates (chromosome , cities) :
    for city in cities :
        if city not in chromosome :
            i = 0
            while i < len (chromosome) :
                j = i + 1
                while j < len (chromosome) :
                    if chromosome [i] == chromosome [j] :
                        chromosome [i] = city

                    j += 1
                i += 1

    return chromosome

def mutation (chromosome) :

    # The mutation operation needs to two genes for swapping genes with each other.

    first = 0           # first gene index
    second = 0          # second gene index

    while first == second :

        # These genes are chosen randomly

        first = randint (1 , len (chromosome) - 1)
        second = randint (1 , len (chromosome) - 1)

    # Genes are moved simultaneously,

    chromosome [first] , chromosome [second] = chromosome [second] , chromosome [first]

    # and returned where called function is.

    return chromosome

if __name__ == "__main__" :
    main ()