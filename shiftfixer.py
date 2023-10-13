import sys

# open source file
sourcefile = sys.argv[1]
source = open(sourcefile)

# open output file
targetfile = sourcefile[0:-6] + "_shiftfixed.gcode"
# force newline character to be unix \n instead of windows \r\n
target = open(targetfile, "w", newline='\n')

count = 0
process = False

for line in source:
  count += 1
  # check for beginning - color change code M600
  if line == "M600\n":
    process = True
  # check for end - disable motors
  if line == "M84 ; disable motors\n":
    process = False  

  if process == True:
    if "G1" in line:
      if "Y" in line:
        split = line.split()
        # element [2] is the Y value
        # extract the numeric Y value from the split
        yvalue = split[2][1:]
        value = float(yvalue)
        # reduce value by 1
        value -= 1.0
        # put value back into string form
        txt = "Y{}"
        split[2] = txt.format(value)
        #print(split[2])
        line = ' '.join(split) + '\n'
        #print(line)

  target.write(line)
  
source.close()
target.close()