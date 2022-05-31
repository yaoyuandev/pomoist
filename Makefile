build:
	python3 setup.py py2app
	zip -r pomoist.zip dist/pomoist.app
clean:
	rm -rf build
	rm -rf dist
