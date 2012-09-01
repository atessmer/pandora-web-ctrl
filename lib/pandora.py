import remote_webkit_debug

__version__ = (0, 1)


class Pandora(object):
   SEL_PLAY = "#playbackControl .playButton"
   SEL_PAUSE = "#playbackControl .pauseButton"
   SEL_SKIP = "#playbackControl .skipButton"
   SEL_THUMB_UP = "#playbackControl .thumbUpButton"
   SEL_THUMB_DOWN = "#playbackControl .thumbDownButton"

   def __init__(self, host='localhost', port=9222):
      self.shell = remote_webkit_debug.ChromeShell(host, port)
      for tab_info in self.shell.get_tabs():
         if "www.pandora.com" in tab_info["url"]:
            self.tab_info = tab_info
            return
      raise Exception("Pandora tab not found.")

   def __enter__(self):
      self.tab = self.shell.pick_tab(self.tab_info)
      return self

   def __exit__(self, exc_type, exc_value, traceback):
      self.tab.__exit__(exc_type, exc_value, traceback)

   def click_str(self, button):
      return "$('%s').click()" % button

   def eval(self, expr):
      return self.tab.send_command("Runtime.evaluate", expression=expr)

   def play(self):
      self.eval(self.click_str(self.SEL_PLAY))

   def pause(self):
      self.eval(self.click_str(self.SEL_PAUSE))

   def play_pause(self):
      play = self.click_str(self.SEL_PLAY)
      pause = self.click_str(self.SEL_PAUSE)
      self.eval("$('%s:visible')[0] ? %s : %s" % (self.SEL_PLAY, play, pause))

   def skip(self):
      self.eval(self.click_str(self.SEL_SKIP))

   def is_playing(self):
      r = self.eval("$('%s:visible')[0]?false:true" % self.SEL_PLAY)
      return r["result"]["result"]["value"]

   def is_paused(self):
      r = self.eval("$('%s:visible')[0]?false:true" % self.SEL_PAUSE)
      return r["result"]["result"]["value"]

   def thumb_up(self):
      self.eval(self.click_str(self.SEL_THUMB_UP))

   def thumb_down(self):
      self.eval(self.click_str(self.SEL_THUMB_DOWN))
