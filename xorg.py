import os

def get_kmap():
    kmap = "us;us;pc105;;"
    filename = None
    if os.access("/etc/X11/xorg.conf", os.R_OK):
        filename = "/etc/X11/xorg.conf"
    elif os.access("/etc/X11/XF86Config", os.R_OK):
        filename = "/etc/X11/XF86Config"
    if filename:
        file = open(filename, 'r')
        layout = None ; variant = None
        import string
        for line in file.readlines():
            list = string.split(line)
            if '"XkbLayout"' in list \
            and list.index('"XkbLayout"') == 1 \
            and list[0] == 'Option' and len(list)>2:
                layout=string.split(list[2],'"')
            if '"XkbVariant"' in list \
            and list.index('"XkbVariant"') == 1 \
            and list[0] == 'Option' and len(list)>2:
                variant=string.split(list[2],'"')
                break
               
    return kmap
