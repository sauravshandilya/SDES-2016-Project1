# stop echo of command on termianl
.SILENT: all		

FILES := researchpaper.tex
AUXFILES := $(FILES:.tex=.aux)
LOGFILES := $(FILES:.tex=.log)
BBLFILES := $(FILES:.tex=.bbl)
BLGFILES := $(FILES:.tex=.blg)

# && \ used to run command as it is running in single shell.
all:
	cd sources/latex-files && \
	pdflatex researchpaper && \
	bibtex researchpaper && \
	pdflatex researchpaper  && \
	pdflatex researchpaper  && \
	#cp *.pdf ../
	mv *.pdf ../output/153076004.pdf
	
clean:
	cd sources/latex-files && \
	$(RM) $(AUXFILES) $(LOGFILES) $(BBLFILES) $(BLGFILES) && \
	cd ../python-files && \
	rm -f *.pyc && \
