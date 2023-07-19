# Lexart_Test_Algorithm

- General Requirements

Algorithms and Data Structure
Idea
We want to circulate a particle inside a cyclotron. The particles used are: e, p, n (electron, proton, and neutron). Each particle has a circulation function within the cyclotron, which can create either a closed or an open cycle.

Find the algorithm that satisfies the following cases for each particle:
Input
[particle, matrix] ~> Example: cyclotron(“e”, matrix)

Outputs
Cyclotron without particles:

[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 1, 1]

Accelerating an electron: 

[e, e, e, e]
[1, 1, 1, e]
[1, 1, 1, e]
[1, 1, 1, e]

Accelerating a proton:

Case: 4x4

[p, p, p, p]
[p, 1, 1, p]
[p, 1, p, p]
[p, p, p, 1]


Case: 6x6

[ p, p, p, p, p, p ]
[ p, 1, 1, 1, 1, p ]
[ p, 1, 1, 1, 1, p ]
[ p, 1, 1, 1, 1, p ]
[ p, 1, 1, 1, p, p ]
[ p, p, p, p, p, 1 ]


Accelerating a neutron:

[n, n, n, n]
[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 1, 1]

- To use

 By default, if the user doesn't provide any input, the program should print the 1 x n matrix. The algorithm is divided into the main application and the auxiliary function (side.py). To use it, you should run the main_algorithm.py file.

 -Example of use

matrix = create_matrix(4)
result = cyclotron(matrix)
for row in result:
    print(row)

or 

matrix = create_matrix("n", 4)
result = cyclotron(matrix)
for row in result:
    print(row)

You can specify the p, n, or e arguments in the 'particle' parameter. If none is given, the program should print the default output.

[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 1, 1]




