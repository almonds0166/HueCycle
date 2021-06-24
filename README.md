# HueCycle

Just a Python script to convert a PNG into a GIF by rotating it around the hue spectrum.

Doesn't work with transparency... (yet..?)

Should work for Python 3.6+.

## Example usage

**`input.png`**:

<div align="center"><img src="./input.png" width="50%"></div>

**Command**:

```bash
python huecycle.py input.png output.gif
```

**`output.gif`**:

<div align="center"><img src="./output.gif" width="50%"></div>

## Command-line args

|  Argument  | Arg  | Effect                                                       |
| :--------: | :--: | ------------------------------------------------------------ |
|  `--help`  | `-h` | Prints help leaflet, then exits.                             |
| `--input`  | `-i` | Path to the input PNG. (required)                            |
| `--output` | `-o` | Path to the output GIF. (required)                           |
| `--period` | `-p` | The number of seconds for the image to make a 360 degree hue cycle. Default 10. |
|  `--step`  | `-s` | The number of degrees to increment the picture between GIF frames. Default 5. |



