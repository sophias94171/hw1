# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation|
#%%
import csv
#=======================================

#%% Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106091221.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

#%% Part. 3.1
#=======================================
# Remove HUMD is -99.000 or -999.000
filtered_data = []
for d in data :
   if d['HUMD'] != '-99.000' and d['HUMD'] != '-999.000':
      filtered_data.append(d)
#=======================================

#%% Part. 3.2
# Find out the summation of the HUMD value from C0A880, C0F9A0, C0G640, C0R190, C0X260.
stations = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
humd_lil = []
result_lil = []
for station in stations:
   humd = []
   for d in filtered_data:
      if d['station_id'] == station:
         humd.append(float(d['HUMD']))
      humd_sum = 'None' if len(humd) == 0 else sum(humd)
   result_lil.append([station, humd_sum])
   humd_lil.append([station, humd])
#=======================================

#%% Part. 4
#=======================================
# Print result
target_data = result_lil
print(target_data)
#========================================

