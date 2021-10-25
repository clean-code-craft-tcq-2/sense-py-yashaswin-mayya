import math

# Initializing a dictionary to store computed statistics
statistics_output = {}

def calculateStats(numbers):
  
  # Try block gets executed only if input list contains only numeric data and length is not zero
  try:
    statistics_output["avg"] = sum(numbers) / len(numbers)
    statistics_output["max"] = max(numbers)
    statistics_output["min"] = min(numbers)

  # Returns NaN if input list contains data other than numbers or if list size is zero
  except:
    statistics_output["avg"]=math.nan
    statistics_output["max"]=math.nan
    statistics_output["min"]=math.nan
  
  return statistics_output


# Define a class for Email Alert
class EmailAlert:
  # Initialize objects of the class
  def __init__(self):
    # Email Alert is flase by default. So initializing to that value
    self.emailSent = False


# Define a class for LED Alert
class LEDAlert:
  # Initialize objects of the class
  def __init__(self):
    # LED is OFF by default. So initializing to that value
    self.ledGlows = False


class StatsAlerter:
  # Initialize objects of the class
  # Two parameters are defined during initialization
  def __init__(self, maxThreshold, alertList):
    self.maxThreshold = maxThreshold
    self.alertList = alertList
    

    # This function is to check if input list contains a number greater than a threshold
    # Email Alert is True and LED is turned ON if input is greater than threshold
  def checkAndAlert(self, numbers):
    
    # Check if any data of input list is higher than threshold value 
    if (max(numbers) > self.maxThreshold):
      # Send Email and turn ON LED
      self.alertList[0].emailSent = True
      self.alertList[1].ledGlows = True
