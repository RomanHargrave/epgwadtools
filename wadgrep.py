#!/usr/bin/python

import re
import sys

import omg

def grep(pattern, map_editor):
    search = re.compile(pattern, re.IGNORECASE).search
    line_map = map_sidedefs_to_linedefs(map_editor)
    found = False
    for i, sidedef in enumerate(map_editor.sidedefs):
        if (search(sidedef.tx_up)
            or search(sidedef.tx_mid)
            or search(sidedef.tx_low)):
            found = True
            print 'sidedef', i, 'of linedef', line_map[i]
    if found:
        return 0
    # Traditionally 1, but Python uses that for uncaught exception.
    return 2

def map_sidedefs_to_linedefs(map_editor):
    result = {}
    for i, linedef in enumerate(map_editor.linedefs):
        result[linedef.front] = i
        if linedef.two_sided:
            result[linedef.back] = i
    return result

def main(argv):
    w = omg.WAD(from_file=omg.WadIO(argv[1], mode='rb'))
    return grep(argv[3], omg.MapEditor(w.maps[argv[2]]))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
