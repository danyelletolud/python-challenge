import os
import csv
import pandas as pd


budgetdata = pd.read_csv("budget_data.csv")


print("Financial Analysis")
print("----------------------")


monthcount = len(budgetdata["Date"].unique())
print("Total Months : " + str(monthcount))

totalprofit = int(budgetdata["Profit/Losses"].sum())
print("Total: $" + str(totalprofit))


average = int(budgetdata["Profit/Losses"].mean())
print("Average Change: $" + str(average))

besttoworse = budgetdata.sort_values(["Profit/Losses"], ascending = False)

bestprofit = besttoworse.iloc[0,:]
print("Greatest Increase in Profit:" +str(bestprofit) )

n= len(budgetdata)

worstprofit = besttoworse.iloc[n-1,:]

print("Greatest Decrease in Profit:" +str(worstprofit))



savefile = open("budgetdata.txt",'w')

savefile.write("Financial Analysis \n")
savefile.write("---------------------- \n")
savefile.write("\n Total Months : " + str(monthcount))
savefile.write("\n Total:$" + str(totalprofit))
savefile.write("\n Average Change: $" + str(average))
savefile.write("\n Greatest Increase in Profit: " + str(bestprofit))
savefile.write("\n Greatest Decrease in Profit: " + str(worstprofit))
savefile.close()



