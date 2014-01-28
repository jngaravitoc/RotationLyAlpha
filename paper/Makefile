LATEX = latex
MAIN  = ms

$(MAIN).pdf: 	$(MAIN).tex references.bib
	$(LATEX) $(MAIN).tex 
	bibtex $(MAIN)
	$(LATEX) $(MAIN).tex 
	$(LATEX) $(MAIN).tex 
	dvips	$(MAIN).dvi -o $(MAIN).ps
	ps2pdf $(MAIN).ps 	

clean:
	rm -f $(MAIN).aux
	rm -f $(MAIN).bbl
	rm -f $(MAIN).ps
	rm -f $(MAIN).pdf
	rm -f $(MAIN).blg
	rm -f $(MAIN).log
	rm -f *~
view: 
	open $(MAIN).pdf &

