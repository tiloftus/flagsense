from setuptools import setup, find_packages

setup(
	name="flagsense",
	version="0.1",
	packages=find_packages(include=["flagsense", "flagsense.*"]),
	install_requires=[
		"ultralytics",
		"opencv-python"
	],
)
