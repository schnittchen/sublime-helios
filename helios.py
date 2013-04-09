import sublime, sublime_plugin


class HeliosCommand(sublime_plugin.ApplicationCommand):
    def run(self, scheme):
        if not (scheme == "light" or scheme == "dark"):
            return

        self.get_colors_and_theme(scheme)
        self.modify_and_save_settings()
        self.set_theme_in_views()

    def get_colors_and_theme(self, scheme):
        settings = sublime.load_settings("Helios.sublime-settings")

        self.colors = settings.get(scheme + "_color_scheme")
        self.theme = settings.get(scheme + "_theme")

    def modify_and_save_settings(self):
        settings = sublime.load_settings("Preferences.sublime-settings")

        settings.set("color_scheme", self.colors)
        settings.set("theme", self.theme)

        sublime.save_settings("Preferences.sublime-settings")

    def set_theme_in_views(self):
        for window in sublime.windows():
            for view in window.views():
                settings = view.settings()
                # first we set the color_scheme setting, so the view
                # is repainted. then we remove it again, so that subsequent
                # global config changes can take effect
                settings.set("color_scheme", self.colors)
                settings.erase("color_scheme")
