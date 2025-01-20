# data_visualization.py

# Placeholder code for Data Visualization project
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Example 1: Simple Line Plot
def line_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.plot(x, y, label='Sine Wave', color='b')
    plt.title('Sine Wave - Line Plot')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.show()

# Example 2: Bar Chart
def bar_chart():
    categories = ['Category A', 'Category B', 'Category C', 'Category D']
    values = [10, 20, 15, 30]
    
    plt.bar(categories, values, color='g')
    plt.title('Bar Chart Example')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()

# Example 3: Scatter Plot
def scatter_plot():
    x = np.random.rand(50)
    y = np.random.rand(50)
    
    plt.scatter(x, y, color='r')
    plt.title('Random Scatter Plot')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.show()

# Example 4: Heatmap using Seaborn
def heatmap():
    data = np.random.rand(10, 10)
    sns.heatmap(data, annot=True, cmap='viridis')
    plt.title('Heatmap Example')
    plt.show()

# Main function to run the examples
if __name__ == "__main__":
    line_plot()
    bar_chart()
    scatter_plot()
    heatmap()
