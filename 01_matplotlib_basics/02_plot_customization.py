import matplotlib.pyplot as plt
import numpy as np

# x = np.array([2020,2021,2022,2023,2024,2025])
# y = np.array([15,25,30,44,33,22])

# plt.plot(x,y,marker =".",
#          markersize = 20,
#          markerfacecolor = "cyan",
#          markeredgecolor = "Black",
#          linestyle = "dashed")

# #markersize can be abbreviated to ms
# #markerfacecolor as mfs
# #CAN BE USED AS HEXADECIMALS AND RRGB VALUES AS WELL


#  #If only one argument passed this will be on z axis and put each increment on 1 (0 ma 15 25 ma 1 types)

# plt.plot(x,y,marker =".",
#          linestyle = "dashed")

# ## Standard Markers

# # | Marker Code | Shape / Description | Category |
# # | :--- | :--- | :--- |
# # | `'.'` | Point | Unfilled / Basic |
# # | `','` | Pixel | Unfilled / Basic |
# # | `'o'` | Circle | Filled |
# # | `'v'` | Triangle (Down) | Filled |
# # | `'^'` | Triangle (Up) | Filled |
# # | `'<'` | Triangle (Left) | Filled |
# # | `'>'` | Triangle (Right) | Filled |
# # | `'1'` | Tri-Down | Unfilled |
# # | `'2'` | Tri-Up | Unfilled |
# # | `'3'` | Tri-Left | Unfilled |
# # | `'4'` | Tri-Right | Unfilled |
# # | `'8'` | Octagon | Filled |
# # | `'s'` | Square | Filled |
# # | `'p'` | Pentagon | Filled |
# # | `'P'` | Plus (Bold / Filled) | Filled |
# # | `'*'` | Star | Filled |
# # | `'h'` | Hexagon 1 (Flat sides vertical) | Filled |
# # | `'H'` | Hexagon 2 (Flat sides horizontal) | Filled |
# # | `'+'` | Plus (Cross) | Unfilled |
# # | `'x'` | X (Cross) | Unfilled |
# # | `'X'` | X (Bold / Filled) | Filled |
# # | `'D'` | Diamond | Filled |
# # | `'d'` | Thin Diamond | Filled |
# # | `'\|'` | Vertical Line | Unfilled |
# # | `'_'` | Horizontal Line | Unfilled |
# # | `'none'` / `None` | No marker (default) | None |

# plt.plot(x,y,marker =".",
#          markersize = 40,
#          markerfacecolor = "Red",
#          markeredgecolor = "Pink",
#          linestyle = "dashed",
#          linewidth = 5,
#          color = "black")

# ## Standard Linestyles

# # | Linestyle / Code | Appearance / Description |
# # | :--- | :--- |
# # | `'-'` or `'solid'` | Solid line (default) |
# # | `'--'` or `'dashed'` | Dashed line |
# # | `':'` or `'dotted'` | Dotted line |
# # | `'-.'` or `'dashdot'` | Dash-dot line |
# # | `'none'` or `' '` or `''` | No line (useful if you only want markers) |

# plt.show()

#If there are two lines to be customizeed

x = np.array([2020,2021,2022,2023,2024,2025])
y1 = np.array([15,25,30,44,33,22])
y2 = np.array([17,68,30,94,13,51])

#Make a dictionary and pass it rather than custumiging each line

# line_style = dict(marker =".",
#          markersize = 20,
#          markerfacecolor = "cyan",
#          markeredgecolor = "Black",
#          linestyle = "dashed",
#          linewidth = 4,
#          color= "Black")

# plt.plot(x,y1,**line_style)

# plt.plot(x,y2,**line_style) #** - unpacking the dictonary

# plt.show()

#if we want something custom like linecolour we remove it from the dict and keep in the indiviual blocl

# line_style = dict(marker =".",
#          markersize = 20,
#          markerfacecolor = "cyan",
#          markeredgecolor = "Black",
#          linestyle = "dashed",
#          linewidth = 4
#          )

# plt.plot(x,y1,color = "Blue",**line_style)

# plt.plot(x,y2,color = "Pink",**line_style) #** - unpacking the dictonary

# plt.show()

# #Each line has different colours

# Practice Questions

# Q1. Basic marker + linestyle
# Using the data below, plot a line with:

# Square markers ('s'), markersize 15
# Marker face color "yellow", edge color "black"
# A dotted line, linewidth 3, color "green"
# python
# months = np.array([1, 2, 3, 4, 5, 6])
# sales  = np.array([10, 18, 14, 30, 26, 35])

# months = np.array([1, 2, 3, 4, 5, 6])
# sales  = np.array([10, 18, 14, 30, 26, 35])

# plt.plot(months,sales,marker = 's',
#          mfc = "Yellow",
#          markersize = 15,
#          mec = "Black",
#          linestyle = "dotted",
#          linewidth = 4,
#          color = "green")

# plt.show()
# Q2. Hex and RGB colors
# Plot the same sales data against months, but this time:

# Use a star marker ('*') with markersize 20
# Set markerfacecolor using a hex code (e.g. "#FF5733")
# Set markeredgecolor using an RGB tuple (values between 0 and 1, e.g. (0.2, 0.4, 0.8))
# Use a dash-dot linestyle

months = np.array([1, 2, 3, 4, 5, 6])
sales  = np.array([10, 18, 14, 30, 26, 35])

# plt.plot(months,sales,marker = '*',
#          mfc = "#FF5733",
#          markersize = 20,
#          mec = (0.2, 0.4, 0.8),
#          linestyle = "dashdot",
#          linewidth = 4,
#          color = "green")

# plt.show()

# Q3. Single argument plot
# Plot only sales (do not pass months). Use a diamond marker ('D'). 
# Then write a comment explaining what values appear on the x-axis and why.

# plt.plot(sales,marker = 'D',
#          mfc = "#FF5733",
#          markersize = 20,
#          mec = (0.2, 0.4, 0.8),
#          linestyle = "dashdot",
#          linewidth = 4,
#          color = "green")

# #The value appearing on x-axis is just basic increment of 1 and it points to each change in values
# plt.show()



# Q4. Two lines with a shared style dictionary (the main one)
# Given:

# python
# years   = np.array([2019, 2020, 2021, 2022, 2023, 2024])
# team_a  = np.array([20, 35, 28, 50, 45, 60])
# team_b  = np.array([10, 22, 40, 33, 55, 48])
# Create a dictionary called common_style holding: marker 'o', markersize 12, markerfacecolor "white", markeredgecolor "black", linestyle "dashed", linewidth 2.
# Plot team_a in "red" and team_b in "purple" using **common_style.
# Do not put color inside the dictionary. Write a comment explaining why.

years   = np.array([2019, 2020, 2021, 2022, 2023, 2024])
team_a  = np.array([20, 35, 28, 50, 45, 60])
team_b  = np.array([10, 22, 40, 33, 55, 48])

line_style = dict(marker = "o",
                  markersize = 12,
                  mfc = "white",
                  mec ="black",
                  linestyle = "dashed",
                  linewidth = 2)

plt.plot(years,team_a,color = "red",**line_style)
plt.plot(years,team_b,color = "purple",**line_style)

plt.show()

#the colors are not passed in dict as it each needs a different colour in it

# Q5. Challenge: spot the bug

# python
# style = dict(marker='.', markersize=10, color='black')
# plt.plot(x, y1, color='blue', **style)

#the colour is being mentioned twice here
# What error occurs and why? How do you fix it?