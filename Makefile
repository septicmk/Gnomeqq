.PHONY:clean

clean:
	find . -name "*.so" -o -name "*.pyc" -o -name "*.pyx.md5" -o -name "*.pyd" | xargs rm -f

