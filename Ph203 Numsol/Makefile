# Make images
all: expliciteuler.png globalerrorexp.png totalenergy.png phaseexp.png

# Explicit Images
expliciteuler.png : numsol.py
	python3 numsol.py 0.004 10000 expliciteuler

globalerrorexp.png : numsol.py
	python3 numsol.py 0.005 50000 globalerrorexp

totalenergy.png : numsol.py
	python3 numsol.py 0.004 100000 totalenergy

phaseexp.png : numsol.py 
	python3 numsol.py 0.004 50000 phaseexp

# Implicit Images 
impliciteuler.png : numsolimp.py
	python3 numsolimp.py 0.004 10000 impliciteuler

globalerrorimp.png : numsolimp.py
	python3 numsolimp.py 0.004 50000 globalerrorimp

totalenergyimp.png : numsolimp.py 
	python3 numsolimp.py 0.004 100000 totalenergyimp

phaseimp.png : numsolimp