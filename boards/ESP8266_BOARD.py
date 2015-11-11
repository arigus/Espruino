#!/bin/false
# This file is part of Espruino, a JavaScript interpreter for Microcontrollers
#
# Copyright (C) 2013 Gordon Williams <gw@pur3.co.uk>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# ----------------------------------------------------------------------------------------
# This file contains information for a specific board - the available pins, and where LEDs,
# Buttons, and other in-built peripherals are. It is used to build documentation as well
# as various source and header files for Espruino.
# ----------------------------------------------------------------------------------------

import pinutils;
info = {
 'name'            : "ESP8266 512KB",
 'espruino_page_link' : 'EspruinoESP8266',
 'default_console' : "EV_SERIAL1",
 'default_console_baudrate' : "115200",
 'variables'       : 1023,
 'binary_name'     : 'espruino_esp8266_board',
};
chip = {
  'part'    : "ESP8266",
  'family'  : "ESP8266",
  'package' : "",
  'ram'     : 80,
  'flash'   : 512,
  'speed'   : 80,
  'usart'   : 1,
  'spi'     : 1,
  'i2c'     : 1,
  'adc'     : 1,
  'dac'     : 0,
  'saved_code' : {
    # see https://github.com/espruino/Espruino/wiki/ESP8266-Design-Notes#flash-map-and-access
    'address' : 0x78000,
    'page_size' : 4096,
    'pages' : 3, # there are really 4 pages reserved but we should only need 3
    'flash_available' : 480, # firmware can be up to this size
  },
};
devices = {
};

# left-right, or top-bottom order
board_esp12 = {
    'top' : ['D1', 'D3', 'D5', 'D4', 'D0', 'D2', 'D15', 'GND'],
    'bottom' : ['VCC', 'D13', 'D12', 'D14', 'B16', 'CH_EN', 'A0', 'RESET'],
    'right' : ['D11', 'D8', 'D9', 'D10', 'D7', 'D6'],
};
board_esp12["bottom"].reverse()
board_esp12["right"].reverse()
board_esp12["_css"] = """
#board {
  width:  600px;
  height: 384px;
  left: 50px;
  top: 100px;
  background-image: url(img/ESP8266_12.jpg);
}
#boardcontainer {
  height: 600px;
}
#board #right {
  top: 60px;
  left: 600px;
}
#board #top {
  bottom: 360px;
  left: 195px;
}
#board #bottom  {
  top: 365px;
  left: 195px;
}
#board .rightpin {
  height: 48px;
}
#board .toppin, #board .bottompin {
  width: 44px;
}
""";

# left-right, or top-bottom order
board_esp01 = {
    'left' : ['D3', 'D0', 'D2', 'GND'],
    'right' : ['VCC', 'RESET', 'CH_PD', 'D1'],
    '_hide_not_on_connectors' : True
};
board_esp01["_css"] = """
#board {
  width:  500px;
  height: 299px;
  left: 50px;
  top: 0px;
  background-image: url(img/ESP8266_01.jpg);
}
#boardcontainer {
  height: 300px;
}
#board #right {
  top: 30px;
  left: 200px;
}
#board #left {
  top: 65px;
  right: 80px;
}
#board #right  {
  top: 65px;
  left: 460px;
}
#board .leftpin {
  height: 48px;
}
#board .rightpin {
  height: 48px;
}
""";

boards = [ board_esp12, board_esp01 ];

def get_pins():
  pins = pinutils.generate_pins(0,15)
  pinutils.findpin(pins, "PD1", True)["functions"]["USART1_TX"]=0;
  pinutils.findpin(pins, "PD3", True)["functions"]["USART1_RX"]=0;
  # just fake pins D0 .. D15
  return pins
