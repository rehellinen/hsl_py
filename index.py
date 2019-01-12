from libs.HslCommunication import SiemensS7Net
from libs.HslCommunication import SiemensPLCS
from config.index import Config

siemens = SiemensS7Net(SiemensPLCS.S1500, Config['plc_ip'])
siemens.ConnectServer()

siemens.WriteString("DB1.276", 'aaaaa123')
