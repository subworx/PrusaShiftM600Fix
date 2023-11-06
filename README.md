# Prusa Layer Shift on manual filament change (M600) Fix
A fix for layer shifting after manual filament change (M600) on Prusa MK3S printers.

![left: original sliced model; right: after running shiftfix on the same gcode file](shift.png)
Left: original sliced model; right: after running shiftfix on the same gcode file. Please ignore the stringing :)

I found that whenever I manually change filaments during a print for multi-colored prints, the second part always gets shifted in Y-direction by ~1mm (left in the photo) using PrusaSlicer 2.6.1, MK3S firmware 3.11.0 and Octoprint 1.9.3.

I created a Python script that searches the G-Code for the first occurrence of `M600` (manual filament change), reduces every Y-value starting from there by 1.1, and saves the result as a new G-Code file. This results in the print running as expected (right in the photo).

Depending on your exact results, you can change the amount by which the Y-value is modified.

On multiple filament changes, the amount of shift stays the same after the first M600, so it doesn't matter if you have one or a dozen M600s in your G-Code.

The error is NOT caused by moving any part of the printer or the printer being misadjusted:
- The same print without filament change does not shift layers and looks perfect.
- During changing filament, I didn't touch anything except for the filament itself. Not the bed, not the head (the latter wouldn't explain a Y-axis shift anyway).
- This happens on all kinds of objects. Downloaded STL files, self-made test objects, doesn't matter.

I attached the test object as STL, the generated G-Code, and the shift-fixed variant for you to take a look at and verify. Just open the STL in your slicer, print it once in single color to make sure there are no shifts (there should not be), next add a color change after layer 4 and check your results with and without the script.


# Advice

If the printer detects a crash after changing filaments, the Layer Shift does NOT happen and the shift-fixed G-Code will cause a layer shift into the opposite direction instead.

Since at least I cannot properly reproduce a crash on every change (and it also takes forever... crash, unload filament, load filament, hope it doesn't crash), at least for multi color prints I turned off Crash Detection on the printer.

# Usage

Export the G-Code file, then run 

`python shiftfix.py "your_file.gcode"`

which results in `"your_file_shiftfixed.gcode"`. Send this file to the printer or save on SD.

You can also place the script on the Raspberry Pi directly and run it in a shell there after uploading your gcode from PrusaSlicer.

Since I have no idea about coding, if someone else wants to put this into an Octoprint plugin that can run the script on selected (or all incoming) files, go for it and please let me know :)
