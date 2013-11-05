TARGET=webdev-presentation
HTML=main_html
SRC={$TARGET}

default: pdf

both: pdf html

dvi: webdev-presentation.tex 
#	pygmentize the input source file -- THIS NAME SHOULD BE SAFE
#	pygmentize -f latex -o __webdev-presentation.tex webdev-presentation.tex
#	run latex twice to get references correct
	latex webdev-presentation.tex
#	you can also have a bibtex line here
#	bibtex webdev-presentation
	latex webdev-presentation.tex
#	remove the pygmentized output to avoid cluttering up the directory
#	rm __webdev-presentation.tex

ps: dvi
	dvips -R -Poutline -t letter webdev-presentation.dvi -o webdev-presentation.ps

pdf: ps
	ps2pdf webdev-presentation.ps

