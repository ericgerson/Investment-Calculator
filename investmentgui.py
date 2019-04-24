""" 
Program : investmentgui.py
Author: Eric
Date: 3/26/19

GUI based version of the Chapter 3 investment calculator.
Focuses on the use of the Text Area widget for display

"""

from breezypythongui import EasyFrame

class TextAreaDemo(EasyFrame):

	def __init__(self):
		"""Sets up the window and widgets"""
		EasyFrame.__init__(self, title ="Investment Calculator")
		
		# All labels for the first 3 rows
		self.addLabel(text = "Initial amount", row = 0, column = 0)
		self.addLabel(text = "Number of years", row = 1, column = 0)
		self.addLabel(text = "Interest rate in %", row = 2, column = 0)
		
		# All the input fields for the first 3 rows
		self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
		self.period = self.addIntegerField(value = 0, row = 1, column = 1)
		self.rate = self.addIntegerField(value = 0, row = 2, column  = 1)
		
		# Command button which handles the compute function
		self.compute = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		
		# Text area field to display the output 
		self.outputArea = self.addTextArea(text = "", row = 4, column = 0, columnspan = 2, width = 50, height = 15)
		
	# Event handling method
	def compute(self):
		"""Computes the investment schedule based on the inputs and outputs the schedule"""
		
		# Obtain and validate the inputs 
		startBalance = self.amount.getNumber()
		rate = self.amount.getNumber() / 100
		years = self.period.getNumber()
		if startBalance == 0 or rate == 0 or years == 0:
		  return 
		 
		# Set the header for the table 
		result = "%4s%18s%10s%16s\n" % ("Year", "Starting Balance", "Interest", "Ending Balance")
		
		
		# Compute and append the results for each year
		totalInterest = 0.0
		for year in range (1, years + 1): 
			interest = startBalance * rate
			endBalance = startBalance + interest 
			result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
			startBalance = endBalance
			totalInterest += interest
			
		# Append the totals for the period
		result += "Ending balance: $%0.2f\n" % endBalance
		result += "Total interest earned: $%0.2f\n" % totalInterest
		
		# Output the results while preserving read-only status
		self.outputArea["state"] = "normal"
		self.outputArea.setText(result)
		self.outputArea["state"] = "disabled"

def main():
	TextAreaDemo().mainloop()

main()