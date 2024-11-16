import matplotlib.pyplot as plt
# Add a plot or subplot to the figure
#The plot function marks the x-coordinates and y-coordinates
plt.plot([1, 2, 3], [4, 5, 6], color="red")
plt.xlim(1, 5)
plt.ylim(1, 6)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
#plt.title('line Graph’)
plt.legend(['Values'])
plt.show()