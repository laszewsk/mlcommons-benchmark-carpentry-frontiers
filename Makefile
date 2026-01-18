# Main document
MAIN = vonLaszewski-mlcommons-benchmark-carpentry

# Compilers
LATEX = pdflatex
BIBER = biber
BIBTEX = bibtex

# Compilation flags
LATEXFLAGS = -interaction=nonstopmode -halt-on-error

# Files to clean
CLEANFILES = *.bbl *.aux *.log *.blg *.bcf *.toc *.out *.lof *.lot *.fls *.fdb_latexmk *.run.xml

.PHONY: all clean view zip

# Default target
all: biblatex

biblatex: clean
	cp $(MAIN)-biblatex.tex $(MAIN).tex
	$(LATEX) $(LATEXFLAGS) $(MAIN).tex
	$(BIBER) $(MAIN)
	$(LATEX) $(LATEXFLAGS) $(MAIN).tex
	$(LATEX) $(LATEXFLAGS) $(MAIN).tex


bibtex: clean
	rm -f *.bbl *.aux
	cp $(MAIN)-bibtex.tex $(MAIN).tex
	$(LATEX) $(MAIN).tex
	$(BIBTEX) $(MAIN)
	$(LATEX) $(MAIN).tex
	$(LATEX)  $(MAIN).tex

# Open PDF
view:
	open $(MAIN).pdf

# Clean auxiliary files
clean:
	@echo "Cleaning auxiliary files..."
	rm -f $(MAIN).pdf $(CLEANFILES)
	@echo "Clean complete!"

# Create zip archive for submission
zip:
	@echo "Creating zip archive..."
	zip -r arxiv-carpentry.zip *.tex *.bib *.bbl images ontology *.cls *.bst \
    		-x vonLaszewski-mlcommons-benchmark-carpentry-biblatex.tex \
       		   vonLaszewski-mlcommons-benchmark-carpentry-bibtex.tex
	@echo "Zip archive created: arxiv-carpentry.zip"


	@echo "Creating zip archive..."
	zip -r arxiv-carpentry.zip *.tex *.bib *.bbl images ontology *.cls *.bst
	@echo "Zip archive created: arxiv-carpentry.zip"

log:
	open -a Aquamacs vonLaszewski-mlcommons-benchmark-carpentry.log
