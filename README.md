# hw1

## Object

- Remove the data whose value of the HUMD (humidity) column is '-99.000' or '-999.000'.
- Find out the summation of the HUMD value from C0A880, C0F9A0, C0G640, C0R190, C0X260.
- Output the ID of the station and the summation of it in the lexicographical order.
- If you cannot find the summation, please output 'None'.

## Usage

### Part. 1 
Import Modulo
```
import csv
```
csv -- fileIO operation|

### Part. 2 
Read cwb Weather Data
```
cwb_filename = '106091221.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
```
### Part. 3.1 
Remove HUMD is -99.000 or -999.000
```
filtered_data = []
for d in data :
   if d['HUMD'] != '-99.000' and d['HUMD'] != '-999.000':
      filtered_data.append(d)
```
### Part. 3.2 
Find out the summation of the HUMD value from C0A880, C0F9A0, C0G640, C0R190, C0X260.
```
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
```   
### Part. 4 
Print result
```   
target_data = result_lil
print(target_data)
```   
## Output Results

Running `$ python hw1` will get the following results
```
[['C0A880', 21.61], ['C0F9A0', 19.79], ['C0G640', 20.669999999999998], ['C0R190', 16.580000000000002], ['C0X260', 20.220000000000006]]
```
