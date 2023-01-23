#!/usr/bin/env python
# Copyright (c) Mon Jan 23 10:52:34 PST 2023 The chromeOSLinux Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Python script to call chromeOSLinuxcycle. This is needed to let the 
# hotkeys ctr-shift-alt F1/F2 work when kodi is in fullscreen.
import subprocess
import sys

if len(sys.argv) == 2 and sys.argv[1] in ("prev", "next"):
  exitcode = subprocess.call(["/usr/local/bin/chromeOSLinuxcycle", sys.argv[1]])
else:
  sys.stderr.write("Usage: %s prev|next\n" % str(sys.argv[0]))
  exitcode = 2
sys.exit(exitcode)
