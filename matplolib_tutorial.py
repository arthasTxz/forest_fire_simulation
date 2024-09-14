import matplotlib.pyplot as plt
import numpy as np
import random

grid = [[1 if random.random() < 0.5  else 0 for _ in range(3)]  for _ in range(3)]

print(grid)


fig, ax = plt.subplots()
plt.imshow(grid, cmap="gray")

ax.set_xticks([])
ax.set_yticks([])


plt.show()

