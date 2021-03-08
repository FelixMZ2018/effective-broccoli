import os

print("Hello World")

temperature = os.environ['TEMPERATURE']
light_sensor = os.environ['LIGHT']
No_of_Soil = os.environ['SOIL'] 
print(f'Using {temperature} as temperature sensor')
print(f'Using {light_sensor} as light sensor')
print(f'confiuration for {No_of_Soil} soil moisture sensors')