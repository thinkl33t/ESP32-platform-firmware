import term, appglue, sys, badge, easydraw

easydraw.msg("This app can only be controlled using the USB-serial connection.", "Notice", True)

term.header(True, "Hours from UTC")
offset = badge.nvs_get_int("badge", "time.offset", "")
offset = term.prompt("Offset", 1, 3, offset)
try:
    offset = int(offset)
    badge.nvs_set_int("badge", "time.offset", offset)
except:
    easydraw.msg("Invalid offset.  Please try again", "Notice", True)
appglue.home()
