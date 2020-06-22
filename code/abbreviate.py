# XXX - would be nice to be able pipe these through formatters

from talon import Context, Module

mod = Module()
mod.list("abbreviation", desc="Common abbreviation")

# TODO: Make this a csv file. Not necessarily a settings/ csv file, it might be
# better to be like homophones.csv.
abbreviations = {
    "address": "addr",
    "administrator": "admin",
    "administrators": "admins",
    "advance": "adv",
    "advanced": "adv",
    "alberta": "ab",
    "alternative": "alt",
    "application": "app",
    "applications": "apps",
    "argument": "arg",
    "arguments": "args",
    "as far as i can tell": "afaict",
    "as far as i know": "afaik",
    "assembly": "asm",
    "at the moment": "atm",
    "attribute": "attr",
    "attributes": "attrs",
    "authenticate": "auth",
    "authentication": "auth",
    "away from keyboard": "afk",
    "binary": "bin",
    "boolean": "bool",
    "british columbia": "bc",
    "button": "btn",
    "canada": "ca",
    "centimeter": "cm",
    "char": "chr",
    "character": "char",
    "class": "cls",
    "client": "cli",
    "command": "cmd",
    "comment": "cmt",
    "compare": "cmp",
    "conference": "conf",
    "config": "cfg",
    "configuration": "cfg",
    "context": "ctx",
    "control": "ctrl",
    "constant": "const",
    "coordinate": "coord",
    "coordinates": "coords",
    "copy": "cpy",
    "count": "cnt",
    "counter": "ctr",
    "database": "db",
    "declare": "decl",
    "declaration": "decl",
    "decode": "dec",
    "decrement": "dec",
    "debug": "dbg",
    "define": "def",
    "definition": "def",
    "description": "desc",
    "develop": "dev",
    "development": "dev",
    "device": "dev",
    "dictation": "dict",
    "dictionary": "dict",
    "direction": "dir",
    "directory": "dir",
    "distribution": "dist",
    "document": "doc",
    "documents": "docs",
    "double": "dbl",
    "dupe": "dup",
    "duplicate": "dup",
    "dynamic": "dyn",
    "encode": "enc",
    "entry": "ent",
    "enumerate": "enum",
    "environment": "env",
    "escape": "esc",
    "etcetera": "etc",
    "example": "ex",
    "exception": "exc",
    "execute": "exec",
    "expression": "exp",
    "extend": "ext",
    "extension": "ext",
    "file system": "fs",
    "framework": "fw",
    "function": "func",
    "funny": "lol",
    "generic": "gen",
    "generate": "gen",
    "hypertext": "http",
    "history": "hist",
    "image": "img",
    "import table": "iat",
    "import address table": "iat",
    "increment": "inc",
    "information": "info",
    "initialize": "init",
    "initializer": "init",
    "in real life": "irl",
    "instance": "inst",
    "integer": "int",
    "interrupt": "int",
    "iterate": "iter",
    "java archive": "jar",
    "javascript": "js",
    "jason": "json",
    "jump": "jmp",
    "keyboard": "kbd",
    "keyword arguments": "kwargs",
    "keyword": "kw",
    "kilogram": "kg",
    "kilometer": "km",
    "language": "lng",
    "length": "len",
    "library": "lib",
    "manitoba": "mb",
    "markdown": "md",
    "message": "msg",
    "meta sploit": "msf",
    "meta sploit framework": "msf",
    "microphone": "mic",
    "milligram": "mg",
    "millisecond": "ms",
    "miscellaneous": "misc",
    "module": "mod",
    "mount": "mnt",
    "nano second": "ns",
    "neo vim": "nvim",
    "new brunswick": "nb",
    "nova scotia": "ns",
    "number": "num",
    "object": "obj",
    "okay": "ok",
    "ontario": "on",
    "option": "opt",
    "operating system": "os",
    "original": "orig",
    "package": "pkg",
    "parameter": "param",
    "parameters": "params",
    "pico second": "ps",
    "pixel": "px",
    "point": "pt",
    "pointer": "ptr",
    "position": "pos",
    "position independent code": "pic",
    "position independent executable": "pie",
    "previous": "prev",
    "property": "prop",
    "public": "pub",
    "python": "py",
    "quebec": "qc",
    "query string": "qs",
    "random": "rnd",
    "receipt": "rcpt",
    "reference": "ref",
    "references": "refs",
    "register": "reg",
    "registery": "reg",
    "regular expression": "regex",
    "regular expressions": "regex",
    "repel": "repl",
    "represent": "repr",
    "representation": "repr",
    "request": "req",
    "return": "ret",
    "revision": "rev",
    "ruby": "rb",
    "rust": "rs",
    "saskatchewan": "sk",
    "service pack": "sp",
    "session id": "sid",
    "shell": "sh",
    "shellcode": "sc",
    "signature": "sig",
    "source": "src",
    "special": "spec",
    "specific": "spec",
    "specification": "spec",
    "specify": "spec",
    "standard in": "stdin",
    "standard out": "stdout",
    "standard": "std",
    "string": "str",
    "structure": "struct",
    "synchronize": "sync",
    "synchronous": "sync",
    "system": "sys",
    "table of contents": "toc",
    "table": "tbl",
    "taiwan": "tw",
    "technology": "tech",
    "temperature": "temp",
    "temporary": "tmp",
    "temp": "tmp",
    "text": "txt",
    "time of check time of use": "toctou",
    "token": "tok",
    "ultimate": "ulti",
    "unique id": "uuid",
    "user": "usr",
    "utilities": "utils",
    "utility": "util",
    "value": "val",
    "variable": "var",
    "verify": "vrfy",
    "versus": "vs",
    "visual": "vis",
    "visual studio": "msvc",
    "web": "www",
    "what the fuck": "wtf",
    "window": "win",
}

ctx = Context()
ctx.lists["user.abbreviation"] = abbreviations
