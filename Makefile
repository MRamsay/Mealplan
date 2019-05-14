
formatter := python3 format_recipes.py recipes.json
in := recipes.md 

all: web pdf md

web: md
	pandoc -i $(in) > recipes.html

pdf: md
	pandoc -i $(in) -o recipes.pdf

md: 
	$(formatter) > $(in)
	cp $(in) README.md

upload: md
	git add README.md
	git commit -m "recipe upload"
	git push


clean:
	rm recipes.pdf recipes.html $(in) README.md
