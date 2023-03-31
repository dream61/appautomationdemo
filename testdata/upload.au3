;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("打开", "","Edit1")


; Wait 10 seconds for the Upload window to appear
  WinWait("[CLASS:#32770]","",10)


; Set the File name text on the Edit field

  ControlSetText("打开", "", "Edit1", "D:\\工作资料\\蒙电通航线管理平台\\航线JSON数据\\220kV_路云线_#2_20210724.json")

  Sleep(2000)

; Click on the Open button

  ControlClick("打开", "","Button1");