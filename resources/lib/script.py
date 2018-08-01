# -*- coding: utf-8 -*-

from resources.lib import kodiutils
from resources.lib import kodilogging
import logging
import xbmcaddon
import xbmcgui
import xbmc
from subprocess import call

logger = logging.getLogger(ADDON.getAddonInfo('mebo.updater'))


# Put your code here, this is just an example showing
# a textbox as soon as this addon gets called
def show_dialog():
    addon_name = ADDON.getAddonInfo('MEBO Updater')

    line1 = "Welcome To The MEBO Updater! \n Please wait while add-ons are installed."

    xbmcgui.Dialog().ok(addon_name, line1)

def download_addons():
    addons = ['plugin.video.aswim']
    for a in addons:
        #call(["cd ~/.kodi/addons; wget %s" % a])
        xbmc.InstallAddon(a)
        xbmc.Notification('Plugin Installed','You can now use this plugin!')
