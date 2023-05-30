import numpy as np
from matplotlib import pyplot as plt
x=np.arange(1,11)
y=3*x
plt.plot(x,y,color='g',linestyle=':',linewidth=5)
plt.title("Line Plot")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.show()


#adding two lines in the same plot
y1=x**2
y2=3*x
plt.plot(x,y1)
plt.plot(x,y2)
plt.grid(True)
plt.title("Two lines in the same plot")
plt.xlabel("Xlabel")
plt.ylabel("Y label")
plt.show()

# subplots
plt.subplot(1,2,1)
plt.plot(x,y1)
plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title("Subplots")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.show()

# Bar plots
student={'Bob':87,'Matt':90,'Sam':27}
names=list(student.keys())
marks=list(student.values())
plt.bar(names,marks)
plt.xlabel("Names")
plt.ylabel("Marks")
plt.title("Bar plot")
plt.show()


# Horizontal bar plots
plt.barh(names,marks)
plt.xlabel("Names")
plt.ylabel("Marks")
plt.title(" Horizontal Bar plot")
plt.show()

# Scatter plot
a=[1,2,3,4,5,6,7,8,9,10]
b=[10,9,8,7,6,5,4,3,2,1]
plt.scatter(a,b,marker='*',c='g',s=100)
plt.title("Scatter plot")
plt.xlabel("Values of a")
plt.ylabel("Values of b")
plt.show()

# Histogarm
a=[1,12,3,45,34,75]
plt.hist(a)
plt.title("Histogram plot")
plt.xlabel("Values of a")
plt.ylabel("Frequency")
plt.show()

# Box Whisker plot
one=[1,2,3,4,5]
two=[10,20,30,40,50]
three=[100,200,300,400,500]
data=list([one,two,three])
plt.boxplot(data)
plt.title("Box whisker plot")
plt.show()

# Violin plot
plt.violinplot(data)
plt.title("Violin plot")
plt.show()


# Pie chart
fruit=['apple','mango','guava','pineapple','grapes']
quantity=[12,34,67,22,78]
plt.pie(quantity, labels=fruit, autopct='%0.1f%%')
plt.show()

# Doughnut chart
plt.pie(quantity,labels=fruit,radius=1.2)
plt.pie([1],colors=['w'],radius=1)
plt.show()