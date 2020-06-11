os: mac
app: Vim
app: Code
app: /.*/
and title: /vim/

-
delete [around] word:
    key(d)
    key(a)
    key(w)

change [inner] word:
    key(c)
    key(i)
    key(w)

change to word <word>:
    key(c)
    key(i)
    key(w)
    dictate.lower(word)
    key(escape)

change until:
    key(d)
    key(t)

delete until:
    key(d)
    key(t)

easy:
    key(,)
    key(,)

easy [motion] up:
    key(,)
    key(,)
    key(k)

easy [motion] down:
    key(,)
    key(,)
    key(j)

delete line:
    key(d)
    key(d)

insert line up:
    key(m)
    key(z)
    key(shift-o)
    key(escape)
    key(`)
    key(z)

insert line down:
    key(m)
    key(z)
    key(o)
    key(escape)
    sleep(50ms)
    key(`)
    key(z)

# normal
slapper:
    key(escape)
    sleep(20ms)
    key(shift-a)
    key(enter)

# colon
coder:
    key(escape)
    sleep(20ms)
    key(shift-a)
    key(:)
    key(enter)

# brace
croaker:
    key(escape)
    sleep(20ms)
    key(shift-a)
    key(space)
    key({)
    key(enter)

# tabbed
slender:
    key(escape)
    sleep(20ms)
    key(shift-a)
    key(enter)
    key(tab)

# reverse-tabbed
sloper:
    key(escape)
    sleep(20ms)
    key(shift-a)
    key(enter)
    key(backspace)

# comma
caper:
    key(escape)
    sleep(20ms)
    key(shift-a)
    key(,)
    key(enter)

save it:
    key(escape)
    sleep(50ms)
    key(enter)

vertical split:
    key(:)
    key(v)
    key(s)
    key(enter)

horizontal split:
    key(:)
    key(s)
    key(p)
    key(enter)

surround word:
    key(y)
    key(s)
    key(i)
    key(w)

surround inner:
    key(y)
    key(s)
    key(i)

talon files:
    key(esc)
    insert(":TalonFiles")
    key(enter)
    insert(".talon$ ")

talon files <word>:
    key(esc)
    insert(":TalonFiles")
    key(enter)
    insert(".talon$ ")
    insert(word)

talon code:
    key(esc)
    insert(":TalonFiles")
    key(enter)
    insert(".py$ ")

talon code <word>:
    key(esc)
    insert(":TalonFiles")
    key(enter)
    insert(".py$ ")
    insert(word)
