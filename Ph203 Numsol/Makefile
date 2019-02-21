# Make images
all: expliciteuler.png globalerrorexp.png totalenergy.png phaseexp.png impliciteuler.png globalerrorimp.png totalenergyimp.png phaseimp.png truncerror.png phasesymp.png phasesymplarge.png totalenergysym.png numsol.pdf

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

phaseimp.png : numsolimp.py
	python3 numsolimp.py 0.004 50000 phaseimp

# Truncation error images
truncerror.png : numsolimp.py
	python3 truncerror.py

# Symplectic Images
phasesymp.png : numsolsym.py
	python3 numsolsym.py 0.004 50000 phasesymp

phasesymplarge.png : numsolsym.py 
	python3 numsolsym.py 0.04 50000 phasesymplarge

totalenergysym.png : numsolsym.py
	python3 numsolsym.py 0.004 5000 totalenergysym

numsol.pdf : main.tex
	pdflatex main.tex
