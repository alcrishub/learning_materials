import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  os.mkdir(filename)
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  date = datetime.datetime.fromtimestamp(timestamp).date()
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(date))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd