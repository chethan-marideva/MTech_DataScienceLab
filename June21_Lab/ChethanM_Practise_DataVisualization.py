import matplotlib.pyplot as plt
import seaborn as sns

# Plot a histogram of student marks from a list.

marks = [100,99,55, 67, 89, 76, 45, 90, 82, 70, 60, 95, 58, 77, 85]

plt.figure(figsize=(6,6))
plt.hist(marks,bins=4,color='orange',edgecolor='black')
plt.xlabel('marks')
plt.ylabel('number of students')
plt.title('plot of hist of student marks')
#plt.grid(True)
plt.savefig("hist_marks.png")
plt.show()


height = [ 160, 148, 170, 175, 180, 185, 155, 165, 172, 168,165]
weight = [ 55, 60, 65, 70, 75, 80, 52, 58, 67, 63,70]

#Visualize the correlation between height and weight using a scatter plot.
#print(height.__len__)
plt.figure(figsize=(6,6))
plt.scatter(weight,height,color='green')
plt.xlabel('weight')
plt.ylabel('Height')
plt.grid(True)
plt.savefig('scatter_plot.png')
plt.show()

#Plot a bar chart showing different categories of expenses.

expenses = {'Food': 400, 'Rent': 1000, 'Transport': 500, 'Utilities': 100, 'Misc': 200}

plt.figure(figsize=(6,6))
plt.bar(expenses.keys(), expenses.values(), color='orange')
plt.title("Monthly Expenses")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.grid(axis='y')
plt.savefig("bar_expenses.png")
plt.show()

departments = ['IT', 'HR', 'Sales', 'IT', 'Sales', 'HR', 'IT', 'Sales']
salaries = [70000, 50000, 60000, 75000, 62000, 52000, 78000, 61000]

#Use a box plot to visualize salary distributions across departments.
plt.figure(figsize=(6,6))
sns.boxplot(x=departments, y=salaries)
plt.title("Salary Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.grid(True)
plt.savefig("boxplot_salary.png")
plt.show()


# Histogram using sns
sns.histplot(marks, bins=6, kde=True, color='skyblue')
plt.title("Histogram of student marks using sns")
plt.grid(True)
plt.savefig("sns_hist_marks.png")
plt.show()

# Scatter plot using sns
sns.scatterplot(x=height, y=weight)
plt.title("Height vs Weight using sns")
plt.grid(True)
plt.savefig("sns_scatter_height_weight.png")
plt.show()

# Bar chart using sns
sns.barplot(x=list(expenses.keys()), y=list(expenses.values()), palette='Set2')
plt.title("Monthly Expenses (Seaborn)")
plt.grid(axis='y')
plt.savefig("sns_bar_expenses.png")
plt.show()