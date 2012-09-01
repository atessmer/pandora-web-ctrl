#!/usr/bin/env python -W ignore::DeprecationWarning

from lib.pandora import Pandora
import sys


def main():
   cmd = sys.argv[1];

   with Pandora() as p:
      if cmd == "play":
         p.play()
      elif cmd == "pause":
         p.pause()
      elif cmd == "toggle":
         p.play_pause()
      elif cmd == "skip":
         p.skip()
      else:
         print "Unknown cmd '%s'" % cmd
         exit(1)


if __name__ == "__main__":
   main()
