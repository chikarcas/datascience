import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.linspace(-10, 10, 1000)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, sigmoid(x))       # Plot the sine of each x point
plt.xlim(-10,10)
plt.ylim(-0.1,1.1)
plt.show()                   # Display the plotSet-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process