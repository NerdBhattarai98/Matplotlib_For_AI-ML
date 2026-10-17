
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023,2024,2025,2026])
y1 = np.array([15,20,30,20])
y2 = np.array([20,30,20,15])
y3 = np.array([24,34,14,44])

plt.title("classsize",fontsize = 25,
          family = "Arial",
          fontweight = "bold",
          color = "Pink")

plt.xlabel("Year",fontsize = 20,family = "Arial",fontweight = "bold",color ="Maroon")

plt.tick_params(axis = "both",colors = "green")
# plt.tick_params(axis = "both") and select both x-axis only or y-axis only

plt.ylabel("No of Studens",fontsize = 20,family = "Arial",fontweight = "bold",color ="Maroon")
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.xticks(x)# this ticks x axis at only given year in the array
plt.show()

# Practice Questions

# Q1. Title and labels
# Using the data below, plot revenue against years. Then add:

# A title "Company Revenue": fontsize 22, family "Arial", bold, color "navy"
# An x-label "Year" and y-label "Revenue (in lakhs)": fontsize 16, bold, color "darkgreen"
# python
# years   = np.array([2021, 2022, 2023, 2024, 2025])
# revenue = np.array([40, 55, 48, 70, 65])

# years   = np.array([2021, 2022, 2023, 2024, 2025])
# revenue = np.array([40, 55, 48, 70, 65])

# label = dict(fontsize = 16,family = "Arial",fontweight = "bold",color = "darkgreen")
# plt.title("Company Revenue",fontsize = 22,family = "Arial",fontweight = "bold",color = "navy")
# plt.xlabel("Year",**label)
# plt.ylabel("Revenue (In Lakhs)",**label)

# plt.plot(years,revenue)

# plt.show()
# Q2. tick_params and xticks
# Using the same plot as Q1:

# Make the tick labels on both axes red.
# Make the x-axis show only the five years in years, with no decimals like 2021.5.
# Now change the tick color for the y-axis only to blue. (Hint: look at the axis argument.)

# years   = np.array([2021, 2022, 2023, 2024, 2025])
# revenue = np.array([40, 55, 48, 70, 65])

years   = np.array([2021, 2022, 2023, 2024, 2025])
revenue = np.array([40, 55, 48, 70, 65])

label = dict(fontsize = 16,family = "Arial",fontweight = "bold",color = "darkgreen")
plt.title("Company Revenue",fontsize = 22,family = "Arial",fontweight = "bold",color = "navy")
plt.xlabel("Year",**label)
plt.ylabel("Revenue (In Lakhs)",**label)

plt.plot(years,revenue)

plt.xlabel("years")
plt.tick_params(axis = "y",color = "blue")
plt.show()



# Q3. Three lines, full styling

# python
# x  = np.array([2022, 2023, 2024, 2025])
# y1 = np.array([12, 18, 25, 22])
# y2 = np.array([30, 24, 20, 28])
# y3 = np.array([10, 15, 35, 40])

# Plot all three lines with a shared style dictionary (marker 'o', markersize 10, linestyle "dashed"), but with a different color for each line.
#  Add a bold title, both axis labels, green tick labels, and make the x-axis show only the years in x.


x  = np.array([2022, 2023, 2024, 2025])
y1 = np.array([12, 18, 25, 22])
y2 = np.array([30, 24, 20, 28])
y3 = np.array([10, 15, 35, 40])

line_style = dict(
    marker = 'o',
    markersize = 10,
    linestyle = "dashed"
)

plt.plot(x,y1,color = "red",**line_style)
plt.plot(x,y2,color = "blue",**line_style)
plt.plot(x,y3,color = "green",**line_style)

plt.tick_params(axis="both",color = "green")
plt.title("Chart",fontweight = "bold")
plt.xlabel("X")
plt.ylabel(["y1",'y2','y3'])
plt.xticks(x)

plt.show()