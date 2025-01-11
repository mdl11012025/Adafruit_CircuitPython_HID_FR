"""
`adafruit_hid.keyboard_layout_fr.KeyboardLayoutFR`
=======================================================

* Author(s): ChatGPT
"""

from .keyboard_layout_base import KeyboardLayoutBase


class KeyboardLayoutFR(KeyboardLayoutBase):
    """Map ASCII characters to appropriate keypresses on a standard AZERTY PC keyboard.

    Non-ASCII characters and most control characters will raise an exception.
    """

    # The ASCII_TO_KEYCODE bytes object is used as a table to map ASCII 0-127
    # to the corresponding keycode on a French AZERTY keyboard.
    # The logic follows the same approach as the US layout with modifications to fit AZERTY.

    ASCII_TO_KEYCODE = (
        b"\x00"  # NUL
        b"\x00"  # SOH
        b"\x00"  # STX
        b"\x00"  # ETX
        b"\x00"  # EOT
        b"\x00"  # ENQ
        b"\x00"  # ACK
        b"\x00"  # BEL \a
        b"\x2a"  # BS BACKSPACE \b
        b"\x2b"  # TAB \t
        b"\x28"  # LF \n (ENTER)
        b"\x00"  # VT \v
        b"\x00"  # FF \f
        b"\x00"  # CR \r
        b"\x00"  # SO
        b"\x00"  # SI
        b"\x00"  # DLE
        b"\x00"  # DC1
        b"\x00"  # DC2
        b"\x00"  # DC3
        b"\x00"  # DC4
        b"\x00"  # NAK
        b"\x00"  # SYN
        b"\x00"  # ETB
        b"\x00"  # CAN
        b"\x00"  # EM
        b"\x00"  # SUB
        b"\x29"  # ESC
        b"\x00"  # FS
        b"\x00"  # GS
        b"\x00"  # RS
        b"\x00"  # US
        b"\x2c"  # SPACE
        b"\x9e"  # ! x1e|SHIFT_FLAG
        b"\xb4"  # " x34|SHIFT_FLAG (shift ')
        b"\xa0"  # # x20|SHIFT_FLAG (shift 3)
        b"\xa1"  # $ x21|SHIFT_FLAG (shift 4)
        b"\xa2"  # % x22|SHIFT_FLAG (shift 5)
        b"\xa4"  # & x24|SHIFT_FLAG (shift 7)
        b"\x34"  # ' (same as QWERTY)
        b"\xa6"  # ( x26|SHIFT_FLAG (shift 9)
        b"\xa7"  # ) x27|SHIFT_FLAG (shift 0)
        b"\xa5"  # * x25|SHIFT_FLAG (shift 8)
        b"\xae"  # + x2e|SHIFT_FLAG (shift =)
        b"\x36"  # ,
        b"\x2d"  # -
        b"\x37"  # . (same as QWERTY)
        b"\x38"  # /
        b"\x27"  # 0
        b"\x1e"  # 1
        b"\x1f"  # 2
        b"\x20"  # 3
        b"\x21"  # 4
        b"\x22"  # 5
        b"\x23"  # 6
        b"\x24"  # 7
        b"\x25"  # 8
        b"\x26"  # 9
        b"\xb3"  # : (same as QWERTY)
        b"\x33"  # ; (same as QWERTY)
        b"\xb6"  # < x36|SHIFT_FLAG (shift ,)
        b"\x2e"  # =
        b"\xb7"  # > x37|SHIFT_FLAG (shift .)
        b"\xb8"  # ? x38|SHIFT_FLAG (shift /)
        b"\x9f"  # @ x1f|SHIFT_FLAG
        b"\x84"  # A (same as QWERTY)
        b"\x85"  # B (same as QWERTY)
        b"\x86"  # C (same as QWERTY)
        b"\x87"  # D (same as QWERTY)
        b"\x88"  # E (same as QWERTY)
        b"\x89"  # F (same as QWERTY)
        b"\x8a"  # G (same as QWERTY)
        b"\x8b"  # H (same as QWERTY)
        b"\x8c"  # I (same as QWERTY)
        b"\x8d"  # J (same as QWERTY)
        b"\x8e"  # K (same as QWERTY)
        b"\x8f"  # L (same as QWERTY)
        b"\x90"  # M (same as QWERTY)
        b"\x91"  # N (same as QWERTY)
        b"\x92"  # O (same as QWERTY)
        b"\x93"  # P (same as QWERTY)
        b"\x94"  # Q (shifted)
        b"\x95"  # R (shifted)
        b"\x96"  # S (same as QWERTY)
        b"\x97"  # T (same as QWERTY)
        b"\x98"  # U (same as QWERTY)
        b"\x99"  # V (same as QWERTY)
        b"\x9a"  # W (shifted for AZERTY)
        b"\x9b"  # X (same as QWERTY)
        b"\x9c"  # Y (shifted)
        b"\x9d"  # Z (shifted)
        b"\x2f"  # [
        b"\x31"  # \ (backslash)
        b"\x30"  # ]
        b"\xa3"  # ^ x23|SHIFT_FLAG (shift 6)
        b"\xad"  # _ x2d|SHIFT_FLAG (shift -)
        b"\x35"  # `
        b"\x04"  # a
        b"\x05"  # b
        b"\x06"  # c
        b"\x07"  # d
        b"\x08"  # e
        b"\x09"  # f
        b"\x0a"  # g
        b"\x0b"  # h
        b"\x0c"  # i
        b"\x0d"  # j
        b"\x0e"  # k
        b"\x0f"  # l
        b"\x10"  # m
        b"\x11"  # n
        b"\x12"  # o
        b"\x13"  # p
        b"\x14"  # q
        b"\x15"  # r
        b"\x16"  # s
        b"\x17"  # t
        b"\x18"  # u
        b"\x19"  # v
        b"\x1a"  # w
        b"\x1b"  # x
        b"\x1c"  # y
        b"\x1d"  # z
        b"\xaf"  # { x2f|SHIFT_FLAG
        b"\xb1"  # | x31|SHIFT_FLAG
        b"\xb0"  # } x30|SHIFT_FLAG
        b"\xb5"  # ~ x35|SHIFT_FLAG
        b"\x4c"  # DEL DELETE
    )

# Assign AZERTY layout
KeyboardLayout = KeyboardLayoutFR
