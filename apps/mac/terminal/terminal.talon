app: apple_terminal
-
#comment or remove tags for command sets you don't want
tag(): tabs
tag(): terminal
tag(): user.file_manager
tag(): user.generic_terminal
tag(): user.git
tag(): user.kubectl
tag(): user.tabs
tag(): terminal
tag(): user.tmux
tag(): user.file_manager

action(user.file_manager_open_parent):
    insert("cd ..")
    key(enter)
action(app.tab_open):
  key(cmd-t)
action(app.tab_close):
  key(cmd-w)
action(app.tab_next):
  key(ctrl-tab)
action(app.tab_previous):
  key(ctrl-shift-tab)
action(app.window_open):
  key(cmd-n)
action(edit.page_down):
  key(command-pagedown)
action(edit.page_up):
  key(command-pageup)
rerun search:
  key(ctrl-r)
suspend:
  key(ctrl-z)
resume:
  insert("fg")
  key(enter)
run vim: "vim\n"
run tea mux:
    insert("tmux")
    key(enter)
grep: "grep "
git grep: "git grep "
ls: "ls\n"
clear way left:
    key(ctrl-u)

clear way right:
    key(ctrl-k)

clear word left:
    key(ctrl-w)

clear word right:
    key(ctrl-k)

go way left:
    key(ctrl-a)
    key(a)
