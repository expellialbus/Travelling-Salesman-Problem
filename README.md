# Travelling Salesman Problem

## This repository contain an instance of Genetic Algorithm

You can write below command to run this program on the command line :

```
python3 Source.py
```

The functions in **Source.py** file is what they do?

> main

The **main** function is the begin function of the program. This function runs
the **run** function and writes the returning value of **run** function to screen.

> run

This function is responsible for running of the program. It contains number of generation (*this means iteration*) and it is also responsible for finding shortest path among of cities.

> createMap

This function creates city's map and returns map to the **run** function.
It also contains distances among of cities.

> startingPopulation

The function creates the starting population. The number of starting population is chosen randomly and random paths are created according as number of population.

> findPurposeValue

The function finds the best chromosome. The means of best chromosome is what the shortest path. This function uses the **calculateDistance** function to find path between city of interest and its neighbors.

> calculateDistance

The function calculates path between city of interest and its neighbors as explained above.

> crossingOver

The function does crossing over between the best chromosome and the other chromosomes in the rest of population (*The crossing over operation is usually doing among of each chromosomes but this operation is had done that just with the best chromosome at this instance*). It also uses **checkDuplicates** and **mutation** functions. The Crossing Over operation is shown below.

![Crossing Over operation](https://github.com/recep-yildirim/Travelling-Salesman-Problem/blob/master/Images/crossing%20over.png) 

> checkDuplicates

This function checks duplicates among of genes in chromosome while **crossingOver** function run and changes duplicates with genes which has to be in chromosome.

> mutation

This function does mutation between two genes on chromosome. These genes are chosen randomly. The Mutation operation is shown below.

![Mutation operation](https://github.com/recep-yildirim/Travelling-Salesman-Problem/blob/master/Images/mutation.png)
