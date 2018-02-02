require 'gdbm'

gdbm = GDBM.new("fruitstore.db")
gdbm["ananas"] = "3"
gdbm["banana"] = "4"
gdbm["apple"] = "5"
gdbm["ananas"] = "2"
gdbm["monkey"] = "1"
gdbm.close