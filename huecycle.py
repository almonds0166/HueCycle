
import argparse
from pathlib import Path
import math
import colorsys
from typing import Union

from PIL import Image, ImageColor
import numpy as np

class HueCycler:
   """Class that processes the command-line arguments and renders the GIF.
   """
   def __init__(self):
      self.parser = argparse.ArgumentParser(
         description="Turn a .PNG into a .GIF that cycles around the hue spectrum."
      )

      self.parser.add_argument(
         "input",
         metavar="IN",
         type=Path,
         help="Path to the input PNG."
      )
      self.parser.add_argument(
         "output",
         metavar="OUT",
         type=Path,
         help="Path to the output GIF."
      )
      self.parser.add_argument(
         "-p", "--period",
         metavar="N",
         type=int,
         default=10,
         help="The number of seconds for the image to make a 360 degree hue cycle. Default 10."
      )
      self.parser.add_argument(
         "-s", "--step",
         metavar="N",
         type=int,
         default=5,
         help="The number of degrees to increment the picture between GIF frames. Default 5."
      )

      self._parse_args()

   def _parse_args(self):
      """Parse the command-line arguments.
      """
      self.args = self.parser.parse_args()
      
      self.input_file = Path(self.args.input)
      self.output_file = Path(self.args.output)
      self.period = self.args.period
      self.step = self.args.step
      self.ms = math.ceil(1000 * self.period * self.step / 360)
      self.num_frames = math.ceil(360 / self.step)

      self.input_image = Image.open(self.input_file).convert("RGBA")

   def process(self):
      """Render the GIF!
      """
      rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
      hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

      arr = np.array(np.asarray(self.input_image).astype("float"))
      r, g, b, a = np.rollaxis(arr, axis=-1)
      h, s, v = rgb_to_hsv(r, g, b)

      frames = []
      for i in range(1, self.num_frames):
         shift = (i * self.step) / 360
         h_ = (h + shift) % 1.0
         r_, g_, b_ = hsv_to_rgb(h_, s, v)
         arr_ = np.dstack((r_, g_, b_, a))
         frame = Image.fromarray(arr_.astype("uint8"), "RGBA")
         frames.append(frame)

      self.input_image.save(
         self.output_file,
         **self.input_image.info,
         save_all=True,
         append_images=frames,
         optimize=True,
         duration=self.ms,
         loop=0
      )

if __name__ == "__main__":
   hc = HueCycler()
   hc.process()


