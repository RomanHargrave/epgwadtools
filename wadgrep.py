#!/usr/bin/python

import re
import sys

import omg

def find_texture(pattern, map_editor):
    """Yield (linedef, sidedef) numbers for sidedefs with a texture.

    Args:
      pattern: regular expression (case-insensitive) to mach texture name
      map_editor: MapEditor to search
    """
    search = re.compile(pattern, re.IGNORECASE).search
    linedefs = map_editor.linedefs
    line_map = map_sidedefs_to_linedefs(linedefs)
    for i, sidedef in enumerate(map_editor.sidedefs):
        linedef_num = line_map[i]
        if search(sidedef.tx_mid):
            yield linedef_num, i
            continue
        if linedefs[linedef_num].two_sided:
            if search(sidedef.tx_mid) or search(sidedef.tx_low):
                yield linedef_num, i

def map_sidedefs_to_linedefs(linedefs):
    result = {}
    for i, linedef in enumerate(linedefs):
        result[linedef.front] = i
        if linedef.two_sided:
            result[linedef.back] = i
    return result

def lighting(map_editor):
    light_levels = {}
    for sector in map_editor.sectors:
        light_levels[sector.light] = 1
    for light_level in sorted(light_levels):
        print light_level
    return 0

def texgrep(map_editor, pattern):
    found = False
    for linedef_num, sidedef_num in find_texture(pattern, map_editor):
        found = True
        print 'sidedef', sidedef_num, 'of linedef', linedef_num
    if found:
        return 0
    # Traditionally 1, but Python uses that for uncaught exception.
    return 2

def main(argv):
    w = omg.WAD(from_file=omg.WadIO(argv[1], mode='rb'))
    map_editor = omg.MapEditor(w.maps[argv[2]])
    return globals()[argv[3]](map_editor, *argv[4:])

if __name__ == '__main__':
    sys.exit(main(sys.argv))
