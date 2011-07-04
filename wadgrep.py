#!/usr/bin/python

import re
import sys

import omg

def grep(pattern, map_editor):
    search = re.compile(pattern, re.IGNORECASE).search
    linedefs = map_editor.linedefs
    line_map = map_sidedefs_to_linedefs(linedefs)
    found = False
    for i, sidedef in enumerate(map_editor.sidedefs):
        linedef_num = line_map[i]
        if search(sidedef.tx_mid):
            found = True
            print 'sidedef', i, 'of linedef', linedef_num
            continue
        if linedefs[linedef_num].two_sided:
            if search(sidedef.tx_mid) or search(sidedef.tx_low):
                found = True
                print 'sidedef', i, 'of linedef', linedef_num
    if found:
        return 0
    # Traditionally 1, but Python uses that for uncaught exception.
    return 2

def map_sidedefs_to_linedefs(linedefs):
    result = {}
    for i, linedef in enumerate(linedefs):
        result[linedef.front] = i
        if linedef.two_sided:
            result[linedef.back] = i
    return result

def main(argv):
    w = omg.WAD(from_file=omg.WadIO(argv[1], mode='rb'))
    return grep(argv[3], omg.MapEditor(w.maps[argv[2]]))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
