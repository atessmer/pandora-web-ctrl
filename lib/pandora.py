import remote_webkit_debug

__version__ = (0, 1)


class Pandora(object):
   SEL_PLAY = "#playbackControl .playButton"
   SEL_PAUSE = "#playbackControl .pauseButton"
   SEL_SKIP = "#playbackControl .skipButton"

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

   def play(self):
      url = "javascript:" + self.click_str(self.SEL_PLAY)
      self.tab.send_command("Page.navigate", url=url)

   def pause(self):
      url = "javascript:" + self.click_str(self.SEL_PAUSE)
      self.tab.send_command("Page.navigate", url=url)

   def play_pause(self):
      play_url = self.click_str(self.SEL_PLAY)
      pause_url = self.click_str(self.SEL_PAUSE)
      url = "javascript:$('%s:visible')[0] ? %s : %s" % \
            (self.SEL_PLAY, play_url, pause_url)
      self.tab.send_command("Page.navigate", url=url)

   def skip(self):
      url = "javascript:" + self.click_str(self.SEL_SKIP)
      self.tab.send_command("Page.navigate", url=url)
