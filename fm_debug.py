# -*- encoding: utf-8 -*-

import sublime
import sublime_plugin
import os.path

class FmTestSideBarFolderExistsCommand(sublime_plugin.ApplicationCommand):

    def run(self, paths=None):
        if paths is None:
            return sublime.error_message('Call it from the side bar, please')
        max_path_length = len(repr(max(paths, key=lambda path: len(repr(path)))))
        sublime.active_window().run_command('show_panel', {'panel': 'console'})
        print('|', '-' * max_path_length, '| ------ | ------ |')
        print('|', 'Path '.center(max_path_length) + ' | Exists | Is dir |')
        print('|', '-' * max_path_length, '| ------ | ------ |')
        for path in paths:
            print('| {0!r} | {1!r:^6} | {2!r:^6} |'.format(path, os.path.exists(path), os.path.isdir(path)))
