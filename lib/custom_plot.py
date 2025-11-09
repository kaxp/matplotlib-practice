import numpy as np 
import matplotlib.pyplot as plt 

years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

incomes = [55, 56, 58, 60, 65, 72, 73, 74]

income_ticks = list(range(50,82,2))

plt.plot(years, incomes)
plt.title("Income of John in USD", fontsize=20, fontname = "Roboto")
plt.xlabel("Year")
plt.ylabel("Yearly income in USD")
plt.yticks(income_ticks, [f"${x}k" for x in income_ticks])

plt.show()

