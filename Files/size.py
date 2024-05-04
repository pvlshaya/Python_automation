import os

totalSize = 0
for filename in os.listdir('C:\\Users\\Lenovo'):
    if not os.path.isfile(os.path.join('C:\\Users\\Lenovo', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\Lenovo', filename))
print(totalSize)

## Returns the size of all the data  in the C: partition on the machine 