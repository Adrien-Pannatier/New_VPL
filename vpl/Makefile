#	Copyright 2018-2021 ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE,
#	Miniature Mobile Robots group, Switzerland
#	Author: Yves Piguet

#	Licensed under the 3-Clause BSD License;
#	you may not use this file except in compliance with the License.
#	You may obtain a copy of the License at
#	https://opensource.org/licenses/BSD-3-Clause

.PHONY: main
main:	all

include Makefile-jsmin

.PHONY: all
all:\
	cleanh\
	vpl-min.js thymio/thymio.js \
	index-svg.html index-svg-min.html index-classic.html index-classic-min.html


# dependencies
index-classic.html: $(python inlinersrctool.py --input=index-classic-min-template.html --dep)
index-svg.html: $(python inlinersrctool.py --input=index-svg-min-template.html --dep)
index-classic-min.html: $(python inlinersrctool.py --input=index-classic-min-template.html --dep)
index-svg-min.html: $(python inlinersrctool.py --input=index-svg-min-template.html --dep)



%.html: %-template.html
	python inlinersrctool.py --input=$< >$@

thymio/thymio.js: submodules/tdm-js/thymio/thymio.js
	mkdir -p thymio
	cp $< $@

.PHONY: doc
doc: $(JS)
	jsdoc -d=doc-js $^

.PHONY: oh
oh:
	ohcount src

.PHONY: cleanh
cleanh:
	del index-svg-min.html
	del index-svg.html 