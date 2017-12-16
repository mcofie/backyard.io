'''
  This module is responsible for querying and generating the temperature 
  of the soil.
'''

class SoilTemperature:
  # deg => Degrees  && feh => Fahrenheit

  celcius = "23 deg"
  fahrenheit = "200 FR"
   
  def __init__(self,cel,feh):
    self.celcius = cel
    self.fahrenheit = feh

  def current_temperature(self,type="deg"):
    if type == "deg":
      return "Temprature : 56 degrees"
    elif type == "feh":
      return "Temperature : 20 Fahrenheit"
    else:
      return "Invalid SI Unit"