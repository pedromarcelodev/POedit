import sublime, sublime_plugin, time

class PoeditHeadersCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		headers = '# SOME DESCRIPTIVE TITLE\n'
		headers += '# Copyright (C) YEAR Free Software Foundation, Inc.\n'
		headers += '# This file is distributed under the same license as the PACKAGE package.\n'
		headers += '# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.\n'
		headers += '#\n'
		headers += 'msgid ""\n'
		headers += 'msgstr ""\n'
		headers += r'"Project-Id-Version: PACKAGE VERSION\n"'
		headers += '\n'
		headers += '"POT-Creation-Date: ' + time.strftime('%Y-%m-%d ') + time.strftime('%H:%M') + r'-0000\n"'
		headers += '\n'
		headers += r'"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"'
		headers += '\n'
		headers += r'"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"'
		headers += '\n'
		headers += r'"Language-Team: LANGUAGE <LL@li.org>\n"'
		headers += '\n'
		headers += r'"MIME-Version: 1.0\n"'
		headers += '\n'
		headers += r'"Content-Type: text/plain; charset=CHARSET\n"'
		headers += '\n'
		headers += r'"Content-Transfer-Encoding: ENCODING\n"'
		headers += '\n'

		self.view.insert(edit, 0, headers)

class PoeditMsgidCommand(sublime_plugin.TextCommand):
    def run(self, edit):
    	self.edit = edit
    	window = sublime.active_window()
        window.show_input_panel('Insert the text for msgid', '', self.on_done, self.on_change, self.on_cancel)
        
    def on_done(self, input):
    	view = sublime.active_window().active_view()
        point = view.sel()[0].begin()
        msg = '\nmsgid "' + input + '"\n'
        msg += 'msgstr ""\n'

        view.insert(self.edit, point, msg)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass