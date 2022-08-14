#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

Menu,Tray,Icon,%A_ScriptDir%\assets\loading.ico,,0

;________________________________________________________________________________________________________________________________

Run, chrome.exe %A_ScriptDir%\docs\bakkgrounfd.png, , Max
Sleep, 500
Send {F11}

pyt:
Sleep, 200
Run, %A_ScriptDir%\MACIEJ_scouts_snake_project.py, , Max

Sleep 200
Send {F11}
Sleep 500

IniRead, zoomAmount, %A_ScriptDir%\screensize.ini, wheel, amount
Send {LCtrl Down}
Send {WheelUp %zoomAmount%}
Send {LCtrl Up} 

/*
PixelGetColor, OutputVar, 1865, 28
if (OutputVar != 0x000000) {
    IniRead, zoomAmount, %A_ScriptDir%\screensize.ini, wheel, amount
    Send {LCtrl Down}
    Send {WheelUp %zoomAmount%}
    Send {LCtrl Up} 

    PixelGetColor, OutputVar, 1865, 28
    if (OutputVar != 0x000000) {
        Loop {
            Send {LCtrl Down}
            Send {WheelUp}
            Send {LCtrl Up}
            PixelGetColor, OutputVar, 1865, 28
        } Until OutputVar == 0x000000
    }
}
*/
Return


;________________________________________________________________________________________________________________________________

^r::
WinClose, ahk_exe py.exe
Sleep, 100
Gosub, pyt
Return

;________________________________________________________________________________________________________________________________

~Esc:: ExitApp
~*F4:: ExitApp

;________________________________________________________________________________________________________________________________

Up::w
Left::a
Down::s
Right::d

+Up::W
+Left::A
+Down::S
+Right::D