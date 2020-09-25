#!/usr/bin/python

# Variables
transfert = input('Indique si es Envio o Recepcion (E/R): ')
idf = input('Indique el IDF: ')
file_name = input('Indique el nombre del archivo: ')
ftype = input('Indique si es ASCII o BINARY (A/B): ')
fvar = input('Indique si es Fijo o Variable (F/V): ')
size = input('Indique si peso del archivo (0 por defecto): ')

if transfert.lower() == 'e':
    idf_envio = """
CFTRECV     =  {},
    FCODE   =  {},
    FNAME   =  /users/cft00/recept/{}.&IDTU,
    FTYPE   =  {},
    FRECFM  =  {},
    FLRECL  =  {},
    EXEC    =  /users/tcs00/exploit/script/generique/0tx.sh,
    MODE    =  REPLACE,
    FACTION =  DELETE,
    COMMENT = SENTINELTNO
""".format()

