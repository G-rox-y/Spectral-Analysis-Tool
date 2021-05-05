# Spectral-Analysis-Tool
A program for determining the composition of a star using its spectrum (inspired by RSpec)

To use, install python 3.6+, and on the installment options check the box that says: Add to PATH
After installment open the command prompt and type following commands:

pip install --update pip

pip install numpy

pip install matplotlib (must be v3.4.0 or higher)

pip install opencv-python

pip install pandas

# How to use
The first thing you have to do after installation, is run the SAT.py script. When started, navigate to the image you would like to analyse. 

The next thing to do is insert reduction factors,, a reduction factor means how much you want to dim a certain color channel in your image. Tone this with the quantum efficiency of your RGB camera sensors. If you dont want to apply a reduction factor insert 1, if you want do dim the image by x times, insert the number x (also I wouldnt advise going below 1 due to pixel oversaturation)

After that select the intensity threshold to filter out the background, but in such a way that spectrum stays intact (and dont worry about the dots, that noise will be automatically removed). 

Rotate and crop the image using CV2 trackbars. It is important that when you crop, you dont crop the star out, the star has to be in the picture for the program to work.

Next you will have to calibrate the program, to do that the program will ask you the maximal, and the minimal visible wavelength of your camera, that way the program will be able to calibrate to the spectrum.

The program will ask you if you want the graph to be displayed in a logarithmic or a linear way. This doesnt affect anything.

Next smoothen the graph using step size and threshold values, adjust them in such a way that only absorption lines you want to observe have minimal values (experiment a bit with that). When you are done click confirm and the program will display the graph of detected absorption lines and possible things that could have caused it.

Thats it, if you have any questions, or potential bug reports, feel free to ask!
