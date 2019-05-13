
formatter := python3 format_recipes.py recipes.json

all: web pdf md

web:
	$(formatter) | pandoc -i - > recipes.html

pdf:
	$(formatter) | pandoc -i - -o recipes.pdf

md: 
	$(formatter) > recipes.md

clean:
	rm recipes.pdf recipes.html
