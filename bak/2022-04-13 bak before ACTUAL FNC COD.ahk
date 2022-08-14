#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%
#SingleInstance

Menu,Tray,Icon,%A_ScriptDir%\assets\loading.ico,,0

Script:
::
Run, %A_ScriptDir%\MACIEJ_scouts_snake_project.py

Sleep 500
Send {LWin Down}
Send {Up}
Send {LWin Up}
Sleep 200
Send {F11}
Sleep 100
Send {LCtrl Down}
Send {WheelUp 39} ;49
Send {LCtrl Up}
Sleep, 500

ToolTip, "\\windowSetUp", 1800, 1000
Menu,Tray,Icon, %A_ScriptDir%\assets\blue.ico,,0 ;waiting for name & contact
Input, nothin, L1 V ; wait for anykey after title
ToolTip, ";title", 1800, 1000
Sleep, 500
KeyWait, Enter, D ;enter after name
ToolTip, ";name", 1800, 1000
Sleep, 500
KeyWait, Enter, D ;enter after contact details
ToolTip, ";contact", 1800, 1000
Sleep, 500

Menu,Tray,Icon,%A_ScriptDir%\assets\orange.ico,,0
Sleep, 50
Input, nothin, L1 V ; wait for anykey
ToolTip, ";any", 1800, 1000

Menu,Tray,Icon,%A_ScriptDir%\assets\loading.ico,,0
FileRead, msgLine, %A_ScriptDir%\msg.txt ;wait for 'set-up' to be written
Loop
    FileRead, msgLine, %A_ScriptDir%\msg.txt
Until (msgLine != "")
ToolTip, ";slepin", 1800, 1000

Menu,Tray,Icon,%A_ScriptDir%\assets\green.ico,,0
timeLeft := 60
Loop, 60
{
    Tooltip, %timeLeft%, 1800, 1000
    Sleep, 1000
    timeLeft := timeLeft - 1
}

ToolTip, ";awake", 1800, 1000
Menu,Tray,Icon,%A_ScriptDir%\assets\loading.ico,,0
FileAppend, end, %A_ScriptDir%\msg.txt
Menu,Tray,Icon,%A_ScriptDir%\assets\purple.ico,,0
ToolTip, ";endd", 1800, 1000

Input, nothin, L1 V ; wait for anykey
WinClose, A
Reload
Return

!r::
WinClose, A
Reload
Return

~Esc:: ExitApp
~*F4:: ExitApp

Up::w
Left::a
Down::s
Right::d

+Up::W
+Left::A
+Down::S
+Right::D