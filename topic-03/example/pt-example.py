

# This is a custom addition to LCD to display temperature
TMIN = -100
TMAX = 100
def getTemperature():
    return math.floor(js_map(analogRead(A0), 0, 1023, TMIN, TMAX) + 0.5)