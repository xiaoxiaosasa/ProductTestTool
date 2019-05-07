# Generated by h2py from stdin
TCS_MULTILINE = 0x0200
CBRS_ALIGN_LEFT = 0x1000
CBRS_ALIGN_TOP = 0x2000
CBRS_ALIGN_RIGHT = 0x4000
CBRS_ALIGN_BOTTOM = 0x8000
CBRS_ALIGN_ANY = 0xF000
CBRS_BORDER_LEFT = 0x0100
CBRS_BORDER_TOP = 0x0200
CBRS_BORDER_RIGHT = 0x0400
CBRS_BORDER_BOTTOM = 0x0800
CBRS_BORDER_ANY = 0x0F00
CBRS_TOOLTIPS = 0x0010
CBRS_FLYBY = 0x0020
CBRS_FLOAT_MULTI = 0x0040
CBRS_BORDER_3D = 0x0080
CBRS_HIDE_INPLACE = 0x0008
CBRS_SIZE_DYNAMIC = 0x0004
CBRS_SIZE_FIXED = 0x0002
CBRS_FLOATING = 0x0001
CBRS_GRIPPER = 0x00400000
CBRS_ORIENT_HORZ = (CBRS_ALIGN_TOP|CBRS_ALIGN_BOTTOM)
CBRS_ORIENT_VERT = (CBRS_ALIGN_LEFT|CBRS_ALIGN_RIGHT)
CBRS_ORIENT_ANY = (CBRS_ORIENT_HORZ|CBRS_ORIENT_VERT)
CBRS_ALL = 0xFFFF
CBRS_NOALIGN = 0x00000000
CBRS_LEFT = (CBRS_ALIGN_LEFT|CBRS_BORDER_RIGHT)
CBRS_TOP = (CBRS_ALIGN_TOP|CBRS_BORDER_BOTTOM)
CBRS_RIGHT = (CBRS_ALIGN_RIGHT|CBRS_BORDER_LEFT)
CBRS_BOTTOM = (CBRS_ALIGN_BOTTOM|CBRS_BORDER_TOP)
SBPS_NORMAL = 0x0000
SBPS_NOBORDERS = 0x0100
SBPS_POPOUT = 0x0200
SBPS_OWNERDRAW = 0x1000
SBPS_DISABLED = 0x04000000
SBPS_STRETCH = 0x08000000
ID_INDICATOR_EXT = 0xE700
ID_INDICATOR_CAPS = 0xE701
ID_INDICATOR_NUM = 0xE702
ID_INDICATOR_SCRL = 0xE703
ID_INDICATOR_OVR = 0xE704
ID_INDICATOR_REC = 0xE705
ID_INDICATOR_KANA = 0xE706
ID_SEPARATOR = 0
AFX_IDW_CONTROLBAR_FIRST = 0xE800
AFX_IDW_CONTROLBAR_LAST = 0xE8FF
AFX_IDW_TOOLBAR = 0xE800
AFX_IDW_STATUS_BAR = 0xE801
AFX_IDW_PREVIEW_BAR = 0xE802
AFX_IDW_RESIZE_BAR = 0xE803
AFX_IDW_DOCKBAR_TOP = 0xE81B
AFX_IDW_DOCKBAR_LEFT = 0xE81C
AFX_IDW_DOCKBAR_RIGHT = 0xE81D
AFX_IDW_DOCKBAR_BOTTOM = 0xE81E
AFX_IDW_DOCKBAR_FLOAT = 0xE81F
def AFX_CONTROLBAR_MASK(nIDC): return (1 << (nIDC - AFX_IDW_CONTROLBAR_FIRST))

AFX_IDW_PANE_FIRST = 0xE900
AFX_IDW_PANE_LAST = 0xE9ff
AFX_IDW_HSCROLL_FIRST = 0xEA00
AFX_IDW_VSCROLL_FIRST = 0xEA10
AFX_IDW_SIZE_BOX = 0xEA20
AFX_IDW_PANE_SAVE = 0xEA21
AFX_IDS_APP_TITLE = 0xE000
AFX_IDS_IDLEMESSAGE = 0xE001
AFX_IDS_HELPMODEMESSAGE = 0xE002
AFX_IDS_APP_TITLE_EMBEDDING = 0xE003
AFX_IDS_COMPANY_NAME = 0xE004
AFX_IDS_OBJ_TITLE_INPLACE = 0xE005
ID_FILE_NEW = 0xE100
ID_FILE_OPEN = 0xE101
ID_FILE_CLOSE = 0xE102
ID_FILE_SAVE = 0xE103
ID_FILE_SAVE_AS = 0xE104
ID_FILE_PAGE_SETUP = 0xE105
ID_FILE_PRINT_SETUP = 0xE106
ID_FILE_PRINT = 0xE107
ID_FILE_PRINT_DIRECT = 0xE108
ID_FILE_PRINT_PREVIEW = 0xE109
ID_FILE_UPDATE = 0xE10A
ID_FILE_SAVE_COPY_AS = 0xE10B
ID_FILE_SEND_MAIL = 0xE10C
ID_FILE_MRU_FIRST = 0xE110
ID_FILE_MRU_FILE1 = 0xE110
ID_FILE_MRU_FILE2 = 0xE111
ID_FILE_MRU_FILE3 = 0xE112
ID_FILE_MRU_FILE4 = 0xE113
ID_FILE_MRU_FILE5 = 0xE114
ID_FILE_MRU_FILE6 = 0xE115
ID_FILE_MRU_FILE7 = 0xE116
ID_FILE_MRU_FILE8 = 0xE117
ID_FILE_MRU_FILE9 = 0xE118
ID_FILE_MRU_FILE10 = 0xE119
ID_FILE_MRU_FILE11 = 0xE11A
ID_FILE_MRU_FILE12 = 0xE11B
ID_FILE_MRU_FILE13 = 0xE11C
ID_FILE_MRU_FILE14 = 0xE11D
ID_FILE_MRU_FILE15 = 0xE11E
ID_FILE_MRU_FILE16 = 0xE11F
ID_FILE_MRU_LAST = 0xE11F
ID_EDIT_CLEAR = 0xE120
ID_EDIT_CLEAR_ALL = 0xE121
ID_EDIT_COPY = 0xE122
ID_EDIT_CUT = 0xE123
ID_EDIT_FIND = 0xE124
ID_EDIT_PASTE = 0xE125
ID_EDIT_PASTE_LINK = 0xE126
ID_EDIT_PASTE_SPECIAL = 0xE127
ID_EDIT_REPEAT = 0xE128
ID_EDIT_REPLACE = 0xE129
ID_EDIT_SELECT_ALL = 0xE12A
ID_EDIT_UNDO = 0xE12B
ID_EDIT_REDO = 0xE12C
ID_WINDOW_NEW = 0xE130
ID_WINDOW_ARRANGE = 0xE131
ID_WINDOW_CASCADE = 0xE132
ID_WINDOW_TILE_HORZ = 0xE133
ID_WINDOW_TILE_VERT = 0xE134
ID_WINDOW_SPLIT = 0xE135
AFX_IDM_WINDOW_FIRST = 0xE130
AFX_IDM_WINDOW_LAST = 0xE13F
AFX_IDM_FIRST_MDICHILD = 0xFF00
ID_APP_ABOUT = 0xE140
ID_APP_EXIT = 0xE141
ID_HELP_INDEX = 0xE142
ID_HELP_FINDER = 0xE143
ID_HELP_USING = 0xE144
ID_CONTEXT_HELP = 0xE145
ID_HELP = 0xE146
ID_DEFAULT_HELP = 0xE147
ID_NEXT_PANE = 0xE150
ID_PREV_PANE = 0xE151
ID_FORMAT_FONT = 0xE160
ID_OLE_INSERT_NEW = 0xE200
ID_OLE_EDIT_LINKS = 0xE201
ID_OLE_EDIT_CONVERT = 0xE202
ID_OLE_EDIT_CHANGE_ICON = 0xE203
ID_OLE_EDIT_PROPERTIES = 0xE204
ID_OLE_VERB_FIRST = 0xE210
ID_OLE_VERB_LAST = 0xE21F
AFX_ID_PREVIEW_CLOSE = 0xE300
AFX_ID_PREVIEW_NUMPAGE = 0xE301
AFX_ID_PREVIEW_NEXT = 0xE302
AFX_ID_PREVIEW_PREV = 0xE303
AFX_ID_PREVIEW_PRINT = 0xE304
AFX_ID_PREVIEW_ZOOMIN = 0xE305
AFX_ID_PREVIEW_ZOOMOUT = 0xE306
ID_VIEW_TOOLBAR = 0xE800
ID_VIEW_STATUS_BAR = 0xE801
ID_RECORD_FIRST = 0xE900
ID_RECORD_LAST = 0xE901
ID_RECORD_NEXT = 0xE902
ID_RECORD_PREV = 0xE903
IDC_STATIC = (-1)
AFX_IDS_SCFIRST = 0xEF00
AFX_IDS_SCSIZE = 0xEF00
AFX_IDS_SCMOVE = 0xEF01
AFX_IDS_SCMINIMIZE = 0xEF02
AFX_IDS_SCMAXIMIZE = 0xEF03
AFX_IDS_SCNEXTWINDOW = 0xEF04
AFX_IDS_SCPREVWINDOW = 0xEF05
AFX_IDS_SCCLOSE = 0xEF06
AFX_IDS_SCRESTORE = 0xEF12
AFX_IDS_SCTASKLIST = 0xEF13
AFX_IDS_MDICHILD = 0xEF1F
AFX_IDS_DESKACCESSORY = 0xEFDA
AFX_IDS_OPENFILE = 0xF000
AFX_IDS_SAVEFILE = 0xF001
AFX_IDS_ALLFILTER = 0xF002
AFX_IDS_UNTITLED = 0xF003
AFX_IDS_SAVEFILECOPY = 0xF004
AFX_IDS_PREVIEW_CLOSE = 0xF005
AFX_IDS_UNNAMED_FILE = 0xF006
AFX_IDS_ABOUT = 0xF010
AFX_IDS_HIDE = 0xF011
AFX_IDP_NO_ERROR_AVAILABLE = 0xF020
AFX_IDS_NOT_SUPPORTED_EXCEPTION = 0xF021
AFX_IDS_RESOURCE_EXCEPTION = 0xF022
AFX_IDS_MEMORY_EXCEPTION = 0xF023
AFX_IDS_USER_EXCEPTION = 0xF024
AFX_IDS_PRINTONPORT = 0xF040
AFX_IDS_ONEPAGE = 0xF041
AFX_IDS_TWOPAGE = 0xF042
AFX_IDS_PRINTPAGENUM = 0xF043
AFX_IDS_PREVIEWPAGEDESC = 0xF044
AFX_IDS_PRINTDEFAULTEXT = 0xF045
AFX_IDS_PRINTDEFAULT = 0xF046
AFX_IDS_PRINTFILTER = 0xF047
AFX_IDS_PRINTCAPTION = 0xF048
AFX_IDS_PRINTTOFILE = 0xF049
AFX_IDS_OBJECT_MENUITEM = 0xF080
AFX_IDS_EDIT_VERB = 0xF081
AFX_IDS_ACTIVATE_VERB = 0xF082
AFX_IDS_CHANGE_LINK = 0xF083
AFX_IDS_AUTO = 0xF084
AFX_IDS_MANUAL = 0xF085
AFX_IDS_FROZEN = 0xF086
AFX_IDS_ALL_FILES = 0xF087
AFX_IDS_SAVE_MENU = 0xF088
AFX_IDS_UPDATE_MENU = 0xF089
AFX_IDS_SAVE_AS_MENU = 0xF08A
AFX_IDS_SAVE_COPY_AS_MENU = 0xF08B
AFX_IDS_EXIT_MENU = 0xF08C
AFX_IDS_UPDATING_ITEMS = 0xF08D
AFX_IDS_METAFILE_FORMAT = 0xF08E
AFX_IDS_DIB_FORMAT = 0xF08F
AFX_IDS_BITMAP_FORMAT = 0xF090
AFX_IDS_LINKSOURCE_FORMAT = 0xF091
AFX_IDS_EMBED_FORMAT = 0xF092
AFX_IDS_PASTELINKEDTYPE = 0xF094
AFX_IDS_UNKNOWNTYPE = 0xF095
AFX_IDS_RTF_FORMAT = 0xF096
AFX_IDS_TEXT_FORMAT = 0xF097
AFX_IDS_INVALID_CURRENCY = 0xF098
AFX_IDS_INVALID_DATETIME = 0xF099
AFX_IDS_INVALID_DATETIMESPAN = 0xF09A
AFX_IDP_INVALID_FILENAME = 0xF100
AFX_IDP_FAILED_TO_OPEN_DOC = 0xF101
AFX_IDP_FAILED_TO_SAVE_DOC = 0xF102
AFX_IDP_ASK_TO_SAVE = 0xF103
AFX_IDP_FAILED_TO_CREATE_DOC = 0xF104
AFX_IDP_FILE_TOO_LARGE = 0xF105
AFX_IDP_FAILED_TO_START_PRINT = 0xF106
AFX_IDP_FAILED_TO_LAUNCH_HELP = 0xF107
AFX_IDP_INTERNAL_FAILURE = 0xF108
AFX_IDP_COMMAND_FAILURE = 0xF109
AFX_IDP_FAILED_MEMORY_ALLOC = 0xF10A
AFX_IDP_PARSE_INT = 0xF110
AFX_IDP_PARSE_REAL = 0xF111
AFX_IDP_PARSE_INT_RANGE = 0xF112
AFX_IDP_PARSE_REAL_RANGE = 0xF113
AFX_IDP_PARSE_STRING_SIZE = 0xF114
AFX_IDP_PARSE_RADIO_BUTTON = 0xF115
AFX_IDP_PARSE_BYTE = 0xF116
AFX_IDP_PARSE_UINT = 0xF117
AFX_IDP_PARSE_DATETIME = 0xF118
AFX_IDP_PARSE_CURRENCY = 0xF119
AFX_IDP_FAILED_INVALID_FORMAT = 0xF120
AFX_IDP_FAILED_INVALID_PATH = 0xF121
AFX_IDP_FAILED_DISK_FULL = 0xF122
AFX_IDP_FAILED_ACCESS_READ = 0xF123
AFX_IDP_FAILED_ACCESS_WRITE = 0xF124
AFX_IDP_FAILED_IO_ERROR_READ = 0xF125
AFX_IDP_FAILED_IO_ERROR_WRITE = 0xF126
AFX_IDP_STATIC_OBJECT = 0xF180
AFX_IDP_FAILED_TO_CONNECT = 0xF181
AFX_IDP_SERVER_BUSY = 0xF182
AFX_IDP_BAD_VERB = 0xF183
AFX_IDP_FAILED_TO_NOTIFY = 0xF185
AFX_IDP_FAILED_TO_LAUNCH = 0xF186
AFX_IDP_ASK_TO_UPDATE = 0xF187
AFX_IDP_FAILED_TO_UPDATE = 0xF188
AFX_IDP_FAILED_TO_REGISTER = 0xF189
AFX_IDP_FAILED_TO_AUTO_REGISTER = 0xF18A
AFX_IDP_FAILED_TO_CONVERT = 0xF18B
AFX_IDP_GET_NOT_SUPPORTED = 0xF18C
AFX_IDP_SET_NOT_SUPPORTED = 0xF18D
AFX_IDP_ASK_TO_DISCARD = 0xF18E
AFX_IDP_FAILED_TO_CREATE = 0xF18F
AFX_IDP_FAILED_MAPI_LOAD = 0xF190
AFX_IDP_INVALID_MAPI_DLL = 0xF191
AFX_IDP_FAILED_MAPI_SEND = 0xF192
AFX_IDP_FILE_NONE = 0xF1A0
AFX_IDP_FILE_GENERIC = 0xF1A1
AFX_IDP_FILE_NOT_FOUND = 0xF1A2
AFX_IDP_FILE_BAD_PATH = 0xF1A3
AFX_IDP_FILE_TOO_MANY_OPEN = 0xF1A4
AFX_IDP_FILE_ACCESS_DENIED = 0xF1A5
AFX_IDP_FILE_INVALID_FILE = 0xF1A6
AFX_IDP_FILE_REMOVE_CURRENT = 0xF1A7
AFX_IDP_FILE_DIR_FULL = 0xF1A8
AFX_IDP_FILE_BAD_SEEK = 0xF1A9
AFX_IDP_FILE_HARD_IO = 0xF1AA
AFX_IDP_FILE_SHARING = 0xF1AB
AFX_IDP_FILE_LOCKING = 0xF1AC
AFX_IDP_FILE_DISKFULL = 0xF1AD
AFX_IDP_FILE_EOF = 0xF1AE
AFX_IDP_ARCH_NONE = 0xF1B0
AFX_IDP_ARCH_GENERIC = 0xF1B1
AFX_IDP_ARCH_READONLY = 0xF1B2
AFX_IDP_ARCH_ENDOFFILE = 0xF1B3
AFX_IDP_ARCH_WRITEONLY = 0xF1B4
AFX_IDP_ARCH_BADINDEX = 0xF1B5
AFX_IDP_ARCH_BADCLASS = 0xF1B6
AFX_IDP_ARCH_BADSCHEMA = 0xF1B7
AFX_IDS_OCC_SCALEUNITS_PIXELS = 0xF1C0
AFX_IDS_STATUS_FONT = 0xF230
AFX_IDS_TOOLTIP_FONT = 0xF231
AFX_IDS_UNICODE_FONT = 0xF232
AFX_IDS_MINI_FONT = 0xF233
AFX_IDP_SQL_FIRST = 0xF280
AFX_IDP_SQL_CONNECT_FAIL = 0xF281
AFX_IDP_SQL_RECORDSET_FORWARD_ONLY = 0xF282
AFX_IDP_SQL_EMPTY_COLUMN_LIST = 0xF283
AFX_IDP_SQL_FIELD_SCHEMA_MISMATCH = 0xF284
AFX_IDP_SQL_ILLEGAL_MODE = 0xF285
AFX_IDP_SQL_MULTIPLE_ROWS_AFFECTED = 0xF286
AFX_IDP_SQL_NO_CURRENT_RECORD = 0xF287
AFX_IDP_SQL_NO_ROWS_AFFECTED = 0xF288
AFX_IDP_SQL_RECORDSET_READONLY = 0xF289
AFX_IDP_SQL_SQL_NO_TOTAL = 0xF28A
AFX_IDP_SQL_ODBC_LOAD_FAILED = 0xF28B
AFX_IDP_SQL_DYNASET_NOT_SUPPORTED = 0xF28C
AFX_IDP_SQL_SNAPSHOT_NOT_SUPPORTED = 0xF28D
AFX_IDP_SQL_API_CONFORMANCE = 0xF28E
AFX_IDP_SQL_SQL_CONFORMANCE = 0xF28F
AFX_IDP_SQL_NO_DATA_FOUND = 0xF290
AFX_IDP_SQL_ROW_UPDATE_NOT_SUPPORTED = 0xF291
AFX_IDP_SQL_ODBC_V2_REQUIRED = 0xF292
AFX_IDP_SQL_NO_POSITIONED_UPDATES = 0xF293
AFX_IDP_SQL_LOCK_MODE_NOT_SUPPORTED = 0xF294
AFX_IDP_SQL_DATA_TRUNCATED = 0xF295
AFX_IDP_SQL_ROW_FETCH = 0xF296
AFX_IDP_SQL_INCORRECT_ODBC = 0xF297
AFX_IDP_SQL_UPDATE_DELETE_FAILED = 0xF298
AFX_IDP_SQL_DYNAMIC_CURSOR_NOT_SUPPORTED = 0xF299
AFX_IDP_DAO_FIRST = 0xF2A0
AFX_IDP_DAO_ENGINE_INITIALIZATION = 0xF2A0
AFX_IDP_DAO_DFX_BIND = 0xF2A1
AFX_IDP_DAO_OBJECT_NOT_OPEN = 0xF2A2
AFX_IDP_DAO_ROWTOOSHORT = 0xF2A3
AFX_IDP_DAO_BADBINDINFO = 0xF2A4
AFX_IDP_DAO_COLUMNUNAVAILABLE = 0xF2A5
AFX_IDC_LISTBOX = 100
AFX_IDC_CHANGE = 101
AFX_IDC_PRINT_DOCNAME = 201
AFX_IDC_PRINT_PRINTERNAME = 202
AFX_IDC_PRINT_PORTNAME = 203
AFX_IDC_PRINT_PAGENUM = 204
ID_APPLY_NOW = 0x3021
ID_WIZBACK = 0x3023
ID_WIZNEXT = 0x3024
ID_WIZFINISH = 0x3025
AFX_IDC_TAB_CONTROL = 0x3020
AFX_IDD_FILEOPEN = 28676
AFX_IDD_FILESAVE = 28677
AFX_IDD_FONT = 28678
AFX_IDD_COLOR = 28679
AFX_IDD_PRINT = 28680
AFX_IDD_PRINTSETUP = 28681
AFX_IDD_FIND = 28682
AFX_IDD_REPLACE = 28683
AFX_IDD_NEWTYPEDLG = 30721
AFX_IDD_PRINTDLG = 30722
AFX_IDD_PREVIEW_TOOLBAR = 30723
AFX_IDD_PREVIEW_SHORTTOOLBAR = 30731
AFX_IDD_INSERTOBJECT = 30724
AFX_IDD_CHANGEICON = 30725
AFX_IDD_CONVERT = 30726
AFX_IDD_PASTESPECIAL = 30727
AFX_IDD_EDITLINKS = 30728
AFX_IDD_FILEBROWSE = 30729
AFX_IDD_BUSY = 30730
AFX_IDD_OBJECTPROPERTIES = 30732
AFX_IDD_CHANGESOURCE = 30733
AFX_IDC_CONTEXTHELP = 30977
AFX_IDC_MAGNIFY = 30978
AFX_IDC_SMALLARROWS = 30979
AFX_IDC_HSPLITBAR = 30980
AFX_IDC_VSPLITBAR = 30981
AFX_IDC_NODROPCRSR = 30982
AFX_IDC_TRACKNWSE = 30983
AFX_IDC_TRACKNESW = 30984
AFX_IDC_TRACKNS = 30985
AFX_IDC_TRACKWE = 30986
AFX_IDC_TRACK4WAY = 30987
AFX_IDC_MOVE4WAY = 30988
AFX_IDB_MINIFRAME_MENU = 30994
AFX_IDB_CHECKLISTBOX_NT = 30995
AFX_IDB_CHECKLISTBOX_95 = 30996
AFX_IDR_PREVIEW_ACCEL = 30997
AFX_IDI_STD_MDIFRAME = 31233
AFX_IDI_STD_FRAME = 31234
AFX_IDC_FONTPROP = 1000
AFX_IDC_FONTNAMES = 1001
AFX_IDC_FONTSTYLES = 1002
AFX_IDC_FONTSIZES = 1003
AFX_IDC_STRIKEOUT = 1004
AFX_IDC_UNDERLINE = 1005
AFX_IDC_SAMPLEBOX = 1006
AFX_IDC_COLOR_BLACK = 1100
AFX_IDC_COLOR_WHITE = 1101
AFX_IDC_COLOR_RED = 1102
AFX_IDC_COLOR_GREEN = 1103
AFX_IDC_COLOR_BLUE = 1104
AFX_IDC_COLOR_YELLOW = 1105
AFX_IDC_COLOR_MAGENTA = 1106
AFX_IDC_COLOR_CYAN = 1107
AFX_IDC_COLOR_GRAY = 1108
AFX_IDC_COLOR_LIGHTGRAY = 1109
AFX_IDC_COLOR_DARKRED = 1110
AFX_IDC_COLOR_DARKGREEN = 1111
AFX_IDC_COLOR_DARKBLUE = 1112
AFX_IDC_COLOR_LIGHTBROWN = 1113
AFX_IDC_COLOR_DARKMAGENTA = 1114
AFX_IDC_COLOR_DARKCYAN = 1115
AFX_IDC_COLORPROP = 1116
AFX_IDC_SYSTEMCOLORS = 1117
AFX_IDC_PROPNAME = 1201
AFX_IDC_PICTURE = 1202
AFX_IDC_BROWSE = 1203
AFX_IDC_CLEAR = 1204
AFX_IDD_PROPPAGE_COLOR = 32257
AFX_IDD_PROPPAGE_FONT = 32258
AFX_IDD_PROPPAGE_PICTURE = 32259
AFX_IDB_TRUETYPE = 32384
AFX_IDS_PROPPAGE_UNKNOWN = 0xFE01
AFX_IDS_COLOR_DESKTOP = 0xFE04
AFX_IDS_COLOR_APPWORKSPACE = 0xFE05
AFX_IDS_COLOR_WNDBACKGND = 0xFE06
AFX_IDS_COLOR_WNDTEXT = 0xFE07
AFX_IDS_COLOR_MENUBAR = 0xFE08
AFX_IDS_COLOR_MENUTEXT = 0xFE09
AFX_IDS_COLOR_ACTIVEBAR = 0xFE0A
AFX_IDS_COLOR_INACTIVEBAR = 0xFE0B
AFX_IDS_COLOR_ACTIVETEXT = 0xFE0C
AFX_IDS_COLOR_INACTIVETEXT = 0xFE0D
AFX_IDS_COLOR_ACTIVEBORDER = 0xFE0E
AFX_IDS_COLOR_INACTIVEBORDER = 0xFE0F
AFX_IDS_COLOR_WNDFRAME = 0xFE10
AFX_IDS_COLOR_SCROLLBARS = 0xFE11
AFX_IDS_COLOR_BTNFACE = 0xFE12
AFX_IDS_COLOR_BTNSHADOW = 0xFE13
AFX_IDS_COLOR_BTNTEXT = 0xFE14
AFX_IDS_COLOR_BTNHIGHLIGHT = 0xFE15
AFX_IDS_COLOR_DISABLEDTEXT = 0xFE16
AFX_IDS_COLOR_HIGHLIGHT = 0xFE17
AFX_IDS_COLOR_HIGHLIGHTTEXT = 0xFE18
AFX_IDS_REGULAR = 0xFE19
AFX_IDS_BOLD = 0xFE1A
AFX_IDS_ITALIC = 0xFE1B
AFX_IDS_BOLDITALIC = 0xFE1C
AFX_IDS_SAMPLETEXT = 0xFE1D
AFX_IDS_DISPLAYSTRING_FONT = 0xFE1E
AFX_IDS_DISPLAYSTRING_COLOR = 0xFE1F
AFX_IDS_DISPLAYSTRING_PICTURE = 0xFE20
AFX_IDS_PICTUREFILTER = 0xFE21
AFX_IDS_PICTYPE_UNKNOWN = 0xFE22
AFX_IDS_PICTYPE_NONE = 0xFE23
AFX_IDS_PICTYPE_BITMAP = 0xFE24
AFX_IDS_PICTYPE_METAFILE = 0xFE25
AFX_IDS_PICTYPE_ICON = 0xFE26
AFX_IDS_COLOR_PPG = 0xFE28
AFX_IDS_COLOR_PPG_CAPTION = 0xFE29
AFX_IDS_FONT_PPG = 0xFE2A
AFX_IDS_FONT_PPG_CAPTION = 0xFE2B
AFX_IDS_PICTURE_PPG = 0xFE2C
AFX_IDS_PICTURE_PPG_CAPTION = 0xFE2D
AFX_IDS_PICTUREBROWSETITLE = 0xFE30
AFX_IDS_BORDERSTYLE_0 = 0xFE31
AFX_IDS_BORDERSTYLE_1 = 0xFE32
AFX_IDS_VERB_EDIT = 0xFE40
AFX_IDS_VERB_PROPERTIES = 0xFE41
AFX_IDP_PICTURECANTOPEN = 0xFE83
AFX_IDP_PICTURECANTLOAD = 0xFE84
AFX_IDP_PICTURETOOLARGE = 0xFE85
AFX_IDP_PICTUREREADFAILED = 0xFE86
AFX_IDP_E_ILLEGALFUNCTIONCALL = 0xFEA0
AFX_IDP_E_OVERFLOW = 0xFEA1
AFX_IDP_E_OUTOFMEMORY = 0xFEA2
AFX_IDP_E_DIVISIONBYZERO = 0xFEA3
AFX_IDP_E_OUTOFSTRINGSPACE = 0xFEA4
AFX_IDP_E_OUTOFSTACKSPACE = 0xFEA5
AFX_IDP_E_BADFILENAMEORNUMBER = 0xFEA6
AFX_IDP_E_FILENOTFOUND = 0xFEA7
AFX_IDP_E_BADFILEMODE = 0xFEA8
AFX_IDP_E_FILEALREADYOPEN = 0xFEA9
AFX_IDP_E_DEVICEIOERROR = 0xFEAA
AFX_IDP_E_FILEALREADYEXISTS = 0xFEAB
AFX_IDP_E_BADRECORDLENGTH = 0xFEAC
AFX_IDP_E_DISKFULL = 0xFEAD
AFX_IDP_E_BADRECORDNUMBER = 0xFEAE
AFX_IDP_E_BADFILENAME = 0xFEAF
AFX_IDP_E_TOOMANYFILES = 0xFEB0
AFX_IDP_E_DEVICEUNAVAILABLE = 0xFEB1
AFX_IDP_E_PERMISSIONDENIED = 0xFEB2
AFX_IDP_E_DISKNOTREADY = 0xFEB3
AFX_IDP_E_PATHFILEACCESSERROR = 0xFEB4
AFX_IDP_E_PATHNOTFOUND = 0xFEB5
AFX_IDP_E_INVALIDPATTERNSTRING = 0xFEB6
AFX_IDP_E_INVALIDUSEOFNULL = 0xFEB7
AFX_IDP_E_INVALIDFILEFORMAT = 0xFEB8
AFX_IDP_E_INVALIDPROPERTYVALUE = 0xFEB9
AFX_IDP_E_INVALIDPROPERTYARRAYINDEX = 0xFEBA
AFX_IDP_E_SETNOTSUPPORTEDATRUNTIME = 0xFEBB
AFX_IDP_E_SETNOTSUPPORTED = 0xFEBC
AFX_IDP_E_NEEDPROPERTYARRAYINDEX = 0xFEBD
AFX_IDP_E_SETNOTPERMITTED = 0xFEBE
AFX_IDP_E_GETNOTSUPPORTEDATRUNTIME = 0xFEBF
AFX_IDP_E_GETNOTSUPPORTED = 0xFEC0
AFX_IDP_E_PROPERTYNOTFOUND = 0xFEC1
AFX_IDP_E_INVALIDCLIPBOARDFORMAT = 0xFEC2
AFX_IDP_E_INVALIDPICTURE = 0xFEC3
AFX_IDP_E_PRINTERERROR = 0xFEC4
AFX_IDP_E_CANTSAVEFILETOTEMP = 0xFEC5
AFX_IDP_E_SEARCHTEXTNOTFOUND = 0xFEC6
AFX_IDP_E_REPLACEMENTSTOOLONG = 0xFEC7
