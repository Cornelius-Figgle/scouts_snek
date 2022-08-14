#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%
#SingleInstance

Menu,Tray,Icon,%A_ScriptDir%\assets\loading.ico,,0

MsgBox, 4, Setup, Run Setup?
IfMsgBox No
    ExitApp
Run, %A_ScriptDir%\docs\bakkgrounfd.py, , Max

Sleep 200
Send {F11}
Sleep 200

i := 0
Loop {
    Send {LCtrl Down}
    Send {WheelUp}
    Send {LCtrl Up}
    i := i + 1
    PixelGetColor, OutputVar, 1865, 28
} Until OutputVar == 0x000000

IniWrite, %i%, %A_ScriptDir%\screensize.ini, wheel, amount
WinClose, ahk_exe py.exe
MsgBox, 0, Setup, Compleat!
ExitApp
Return ;lmao

~Esc:: ExitApp
~*F4:: ExitApp