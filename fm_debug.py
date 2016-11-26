# -*- encoding: utf-8 -*-

import sublime
import sublime_plugin
import os.path

class FmTestSideBarFolderExistsCommand(sublime_plugin.ApplicationCommand):

    def run(self, paths=None):
        # return sublime.message_dialog(str( len(max('hello', 'hisdfdfds', 'hi', key=lambda path: len(repr(path)))) ))
        if paths is None:
            return sublime.error_message('Call it from the side bar, please')

        # sublime.message_dialog('Have a look in the console (view -> show console)')
        print('File Manager Tests')
        print('Path '.center(len(repr(max(paths, key=lambda path: len(repr(path)))))) + ' | Exists | Is dir')
        print('-' * (len(repr(max(paths, key=lambda path: len(repr(path)))))), '| ------ | ------')
        for path in paths:
            print('{0!r} | {1} | {2}'.format(path, str(os.path.exists(path)).center(6), os.path.isdir(path)))
