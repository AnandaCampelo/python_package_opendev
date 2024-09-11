#!/usr/bin/env python3
from dev_aberto.dev_aberto import hello

import gettext
gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext

# cli é o nome do arquivo em que guardamos nossas traduções
# localedir é o caminho onde estão armazenadas as traduções. Pode ser um caminho relativo. 

if __name__ == '__main__':
    date, name = hello()
    print(_('Last commit made in:'), date, _('by'), name)
