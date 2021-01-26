import numpy as np
import matplotlib.pyplot as plt

our_numbers = np.random.rand(10)
plt.hist(our_numbers)

plt.savefig("our_nice_plot.pdf")
plt.show()

