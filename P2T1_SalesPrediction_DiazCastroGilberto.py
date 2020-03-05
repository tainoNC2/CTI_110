# This project will calculate the Sales Prediction Profit.
# Date 2/20/2020
# CTI-110
# Page 74, no. 2
# DiazCastroGilberto

# Declare variables

projectedSales = 0
profit = 0
PERCENT = .23
totalSales = 0

# Get input

projectedSales = float(input("Enter the projected amount of sales: "))
# print(projectedSales)

# Calculate profit

profit = projectedSales * PERCENT
print("The expected profit on that amount is: $",format(profit,',.2f'))

# Calculate Ntotal sales

totalSales = projectedSales + profit
print("The total sales expected are: $",format(totalSales,',.2f'))
