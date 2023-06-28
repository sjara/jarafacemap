# jarafacemap

*Jarafacemap* is a fork of [FaceMap](https://github.com/MouseLand/facemap ) (version 0.2.0), a tool for processing videos developed by Carsen Stringer and others. In the [Jaramillo lab](https://jaralab.uoregon.edu/), we wanted to have a light interface to look through videos and apply simple measurements (including pixel change measurements), without all the complexity of FaceMap v1.0.

For details, see the [original documentation of FaceMap v0.2.0](https://github.com/MouseLand/facemap/blob/b6334475d71179d440ef3b5c51c7dd93197a5504/README.md)

This fork provides the following changes:
* A new ROI (`pixelchange`) that measures the average pixel changes between frames. Useful for evaluating running.
* Bug fixes when saving/loading ROIs.

## Running jarafacemap in the Jaramillo lab:
First, enable the virtual environment, then run jarafacemap with the flag `-m`.
* `workon jarafacemap`
* `python -m jarafacemap`

## Installation for the Jaramillo lab (Ubuntu 20.04)

1. Clone this repository in your `~/src/` folder:
 * `cd ~/src/`
 * `git clone git://github.com/sjara/jarafacemap.git`
2. Create a virtual environment:
 * `mkvirtualenv jarafacemap`
3. If needed, enable that virtual environment:
 * `workon jarafacemap`
4. Install PyQt5 first (otherwise, installation seems to get stuck):
 * `pip install PyQt5==5.15.6`
5. Install jarafacemap (in development mode):
 * `cd ~/src/jarafacemap/`
 * `pip3 install -e ./` 



