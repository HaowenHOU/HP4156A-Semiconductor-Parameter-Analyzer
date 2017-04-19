# HP4156A-Semiconductor-Parameter-Analyzer
基于python的HP4156A半导体参数分析仪控制代码
HP4156A是惠普经典的半导体参数分析仪。由于年代久远，HP4156A还是使用磁盘读取数据，没有USB接口，需要一套软件将设备控制起来，便于测量信息取出。
## HP4156A.py
用于连接，设置，控制半导体分析仪。内部使用pyvisa来控制GPIB通信，使用ASCII SCPI指令集。基于指令集，可以模拟半导体分析仪的控制面板。具体指令请参看SCPI command reference for HP4156。

##TRANSISTOR_IDVD_DATA_EXTACTION.py
用于测量晶体管的输出特性

##TRANSISTOR_IDVG_DATA_EXTACTION
用于测量晶体管的转移特性

##LED_DATA_EXTACTION
用于测量LED的I-V曲线


