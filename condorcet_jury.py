import matplotlib.pyplot as plt
import numpy as np
import math


def condorcet_jury(N, p):
    """
    Parameters
    ----------
    N: int
        total population of voters 
    p: float 
        average percentage of competence of the voters (0 < comp < 1)

    Returns
    -------
    cr: float
        collective reliability

    """
    cr = 0.0
    m = N//2 + 1
    for i in range(m, N+1):
        term1 = ((math.factorial(N))/(math.factorial(N-i)*math.factorial(i)))
        term2 = p**i
        term3 = (1-p)**(N-i)
        cr += (term1)*(term2)*(term3)
    return cr

x_40 = np.array([i for i in range(1, 1001)])
x_40 = x_40[::2]
y_40 = np.array([condorcet_jury(i, 0.4) for i in range(1, 1001)])
y_40 = y_40[::2]

x_49 = np.array([i for i in range(1, 1001)])
x_49 = x_49[::2]
y_49 = np.array([condorcet_jury(i, 0.49) for i in range(1, 1001)])
y_49 = y_49[::2]

x_50 = [i for i in range(1, 1001)]
x_50 = x_50[::2]
y_50 = [condorcet_jury(i, 0.5) for i in range(1, 1001)]
y_50 = y_50[::2]

x_60 = [i for i in range(1, 1001)]
x_60 = x_60[::2]
y_60 = [condorcet_jury(i, 0.6) for i in range(1, 1001)]
y_60 = y_60[::2]

# Create the scatterplot
plt.plot(x_40, y_40, color='blue', label='40%')
plt.plot(x_49, y_49, color='orange', label='49%')
plt.plot(x_50, y_50, color='red', label='50%')
plt.plot(x_60, y_60, color='green', label='60%')

# Add labels and title
plt.xlabel('Population of Voters')
plt.ylabel('Collective Reliability')
plt.title('Collective Reliability Over Time with Different Competence Levels')
# Add a legend
plt.legend()

# Show the plot
plt.show()

