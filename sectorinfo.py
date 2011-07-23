"""Map sector types to descriptive strings."""

all_desc2num = {}

all_num2desc = {
    0:   "Normal",
    1:   "Light blinks randomly",
    2:   "Light blinks every 0.5 second",
    3:   "Light blinks every second",
    4:   "-10/20% health, light blinks every 0.5 second",
    5:   "-5/10% health",
    7:   "-2/5% health",
    8:   "Light pulsates every 2 seconds",
    9:   "Secret",
    10:  "30s after start, door closes",
    11:  "-10/20% health, end level when health < 11%",
    12:  "Light blinks every 0.5 second, synchronized",
    13:  "Light blinks every 1 second, synchronized",
    14:  "5m after level start, door opens",
    16:  "-10/20% health",
    17:  "Light flickers on and off randomly [v1.6]",
}
