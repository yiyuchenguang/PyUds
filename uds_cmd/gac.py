#!C:\Program Files (x86)\anaconda3_32\python.exe
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:52:26 2019

@author: levy.he
"""
import sys
import os
import re
import pickle
from pyuds import PyUds
from pyuds import Scripts
from datetime import datetime
from termcolor import color, cprint
from ExcelParse import ExcelToJson as EJ

flash_driver = (0x91,0x00,0x80,0xFF,0xD9,0xFF,0x10,0x02,0x54,0xFF,0x16,0x08,0x3B,0x80,0x00,0x00,0x7E,0x03,0x82,0x12,0x00,0x90,0x91,0x00,0xF0,0x2A,0xD9,0x22,0x54,0x55,0xDA,0xFA,0x74,0x2F,0x91,0x30,0x00,0x4F,0x19,0x4F,0x30,0x36,0xB7,0x0F,0x08,0xF0,0x96,0xF1,0x59,0x4F,0x30,0x36,0x0D,0x00,0xC0,0x04,0xB7,0x2F,0x04,0xF0,0x59,0x4F,0x30,0x36,0x0D,0x00,0xC0,0x04,0x91,0x10,0xF0,0x5A,0x59,0x54,0x90,0x9A,0x8F,0xF5,0x0F,0xF1,0x59,0x5F,0x98,0x9A,0xDA,0x80,0x59,0x5F,0xA8,0xAA,0xDA,0x50,0x59,0x5F,0xA8,0xAA,0x0D,0x00,0x80,0x04,0x19,0x4F,0x30,0x36,0xB7,0x0F,0x08,0xF0,0x96,0xF1,0x59,0x4F,0x30,0x36,0x0D,0x00,0xC0,0x04,0xB7,0x3F,0x04,0xF0,0x59,0x4F,0x30,0x36,0x0D,0x00,0xC0,0x04,0x82,0x04,0x02,0x40,0xC5,0xF4,0x10,0x00,0x54,0x41,0xBB,0x00,0x00,0x5B,0x9B,0x15,0xB7,0x50,0x3B,0x00,0x98,0x23,0x9B,0x02,0x60,0x20,0x3C,0x03,0x54,0x40,0xA2,0x10,0x54,0xF3,0x26,0x23,0xF6,0x33,0x3F,0x50,0xFB,0xFF,0x7F,0x50,0x2B,0x80,0x91,0x00,0x80,0x5F,0x39,0x50,0x11,0x02,0x39,0x51,0x11,0x02,0x37,0x01,0xE1,0xF2,0x6F,0x40,0x21,0x80,0xEE,0x1F,0x54,0x41,0x82,0x00,0x3C,0x06,0x54,0xFF,0x2E,0xB2,0x82,0x14,0x54,0x40,0xA2,0x10,0x54,0xFF,0x2E,0x34,0xF6,0x43,0x3F,0x50,0xF8,0xFF,0x91,0x00,0x80,0xFF,0x39,0xFF,0x13,0x02,0x37,0x0F,0x61,0xF1,0x39,0xF1,0x13,0x02,0x37,0x01,0xE1,0x10,0x7F,0x50,0x07,0x80,0xF6,0x46,0xEE,0x02,0x76,0x14,0x82,0x24,0x3C,0x02,0x82,0x14,0x02,0x42,0xDA,0xFA,0x74,0x2F,0x00,0x90,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0x91,0x00,0x80,0xFF,0xD9,0xFF,0x10,0x02,0x82,0x0B,0x20,0x08,0x02,0xB3,0x02,0xB6,0x54,0xF0,0x3B,0x80,0x00,0x10,0x91,0x00,0xF0,0x2A,0xD9,0x22,0x54,0x55,0x8F,0x80,0x00,0xF1,0x7E,0x14,0x82,0x1B,0x1D,0x00,0xDA,0x00,0x3B,0xA0,0x0F,0x10,0x74,0x21,0x3B,0x00,0x28,0x20,0xC5,0xF5,0x10,0x00,0x3B,0x00,0x20,0x73,0x7B,0x00,0xF0,0x8A,0x3B,0x00,0x0A,0x90,0x1D,0x00,0xC8,0x00,0x91,0x30,0x00,0x6F,0xD9,0x66,0x30,0x36,0x54,0x60,0xB7,0x00,0x08,0xF0,0x96,0xF1,0x74,0x6F,0x0D,0x00,0xC0,0x04,0xB7,0x2F,0x04,0x00,0x74,0x60,0x0D,0x00,0xC0,0x04,0xDA,0x50,0x74,0x2F,0x0D,0x00,0x80,0x04,0x54,0x60,0xB7,0x00,0x08,0xF0,0x96,0xF1,0x74,0x6F,0x0D,0x00,0xC0,0x04,0xB7,0x3F,0x04,0xF0,0x74,0x6F,0x0D,0x00,0xC0,0x04,0x54,0x50,0x3C,0x03,0x54,0x56,0xA2,0x06,0x54,0xFF,0x26,0x7F,0xEE,0x03,0x3F,0x26,0xFB,0xFF,0x54,0xFF,0x3B,0x00,0x00,0x02,0x26,0x0F,0x54,0xF0,0x3B,0x00,0x00,0xA1,0x26,0xA0,0x7F,0x26,0x04,0x80,0xEE,0x02,0x76,0x04,0x82,0x1B,0x1D,0x00,0x90,0x00,0x3B,0x00,0x10,0xA0,0x3F,0xA5,0x08,0x80,0x8F,0xF4,0x0F,0xF1,0xEE,0x04,0x3B,0xA0,0x07,0xB0,0x3C,0x05,0x3B,0xA0,0x0A,0xB0,0x3B,0x00,0x02,0xA0,0x54,0x60,0xB7,0x00,0x08,0xF0,0x96,0xF1,0x74,0x6F,0x0D,0x00,0xC0,0x04,0xB7,0x2F,0x04,0x00,0x74,0x60,0x0D,0x00,0xC0,0x04,0x82,0x0C,0x8F,0xEA,0x1F,0x00,0xC2,0xF0,0x60,0x07,0x8F,0x1C,0x00,0xF1,0x8F,0x2F,0x00,0x00,0x1B,0x00,0x5F,0x05,0xA6,0x80,0x60,0x0C,0x44,0x4F,0x74,0xCF,0xC2,0x1C,0xFC,0x75,0x91,0x00,0x80,0x7F,0xD9,0x77,0x11,0x02,0x14,0x7F,0x2E,0x43,0x82,0x1B,0x3C,0x50,0x91,0x10,0xF0,0xCA,0x59,0xC4,0x90,0x9A,0x59,0xC3,0x98,0x9A,0x59,0xC9,0xA8,0xAA,0x59,0xCB,0xA8,0xAA,0x0D,0x00,0x80,0x04,0xDA,0x00,0x74,0xAF,0x54,0x5B,0x3B,0x10,0x38,0xC0,0x06,0x7C,0x3B,0x00,0x98,0xD3,0x9B,0x0D,0x60,0xD0,0x3C,0x03,0x54,0x5F,0xA2,0xBF,0x54,0xF0,0x26,0xD0,0xF6,0x03,0x3F,0xCF,0xFB,0xFF,0x7F,0xCF,0x2A,0x80,0x14,0x70,0x14,0x7F,0x37,0x0F,0xE1,0xF2,0x6F,0x40,0x24,0x80,0xEE,0x22,0x54,0x5B,0x82,0x00,0x3C,0x07,0x54,0xFF,0x2E,0xB3,0xDA,0x01,0x74,0xAF,0x54,0x50,0xA2,0xB0,0x54,0xFF,0x2E,0x35,0x54,0xAF,0xEE,0x03,0x3F,0xC0,0xF6,0xFF,0x91,0x00,0x80,0x7F,0x39,0x7F,0x13,0x02,0x37,0x0F,0x61,0xB1,0x39,0x7F,0x13,0x02,0x37,0x0F,0xE1,0xD0,0x7F,0xC0,0x08,0x80,0x54,0xAF,0xEE,0x07,0xF6,0xB2,0x76,0xD5,0xDA,0x02,0x3C,0x02,0xDA,0x01,0x74,0xAF,0x54,0xAB,0xF6,0xB3,0xA2,0xA5,0x42,0xA4,0x74,0x21,0x54,0x6F,0xB7,0x0F,0x08,0xF0,0x96,0xF1,0x74,0x6F,0x0D,0x00,0xC0,0x04,0xB7,0x3F,0x04,0xF0,0x74,0x6F,0x0D,0x00,0xC0,0x04,0x76,0x53,0xDF,0x0B,0x39,0x7F,0xDA,0xF0,0x74,0x2F,0x02,0xB2,0x00,0x90,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0xAD,0xF0,0x8F,0x00,0x66,0xBF,0x21,0x3E)

can_node_config = (0xFF, 0xFF, 0x1F, 0x00)

car_config = (0xFF, 0x0C, 0x0F, 0x55, 0x03, 0x00, 0x00, 0x00)

dtc_fault_config = None
dtc_fault_pickle_path = 'dtc_fault_config.pick'

class UdsResponseError(Exception):
    pass

Uds_Req_List = (
    "diagRawRequest",
    "diagFuncRequest",
    "SessionControl",
    "ECUReset",
    "ClearDiagnosticInformation",
    "ReadDtcInformation",
    "ReadDataByIdentifier",
    "ReadMemoryByAddress",
    "SecurityAccess",
    "CommunicationControl",
    "ReadDataByPeriodicIdentifier",
    "DynamicallyDefineDataIdentifier",
    "WriteDataByIdentifier",
    "InputOutputControlByIdentifier",
    "RoutineControl",
    "RequestDownload",
    "RequestUpload",
    "TransferData",
    "RequestTransferExit",
    "WriteMemoryByAddress",
    "TesterPresent",
    "ControlDTCSetting"
)

DTC_STATUS = {
    0x00: ("Pass",'green', None, 'bold'),
    0x09: ("Failed",'red', None, 'bold'),
    0x08: ("History", 'white', None, None),
}
UNKNOWN_STATUS = ('Unknown', 'magenta', None, None)

{
    "DTC": ("DTC_Name", "desc")
}
{
    "EventID":("DTC","EVENT_NAME","desc")
}

def DTCFaultConfigLoad(excel_path):
    pick_config = None
    is_update = False
    try:
        with open(dtc_fault_pickle_path, 'rb') as f:
            pick_config = pickle.load(f)
        excel_info = os.stat(excel_path)
        if int(pick_config['excel_mtime']) != int(excel_info.st_mtime):
            is_update = True
    except:
        is_update = True
    finally:
        if is_update:
            try:
                excel_info = os.stat(excel_path)
                config = GetDTCFaultConfig(excel_path)
                pick_config = dict(excel_mtime=excel_info.st_mtime,config=config)
                with open(dtc_fault_pickle_path, 'wb+') as f:
                    pickle.dump(pick_config, f, pickle.HIGHEST_PROTOCOL)
                return config
            except:
                cprint('can not load dtc config from:%s' % (excel_path), fg='red', attrs='bold')
                return None
        else:
            return pick_config['config']

def GetDTCFaultConfig(excel_path):
    dtc_sheet = 'ACCT DTCs'
    fault_sheet = 'ACCT Autoliv Faults'
    dtc_cols = [0, 1, 2, 3]
    fault_cols = [0, 3, 5, 6, 20]
    config = EJ(excel_path)
    dtc_json = config.GetSheetJsonByCols(dtc_sheet, *dtc_cols, start_row=1)
    fault_json = config.GetSheetJsonByCols(fault_sheet, *fault_cols, start_row=4)
    config.work_book_close()
    DTCs = {}
    for d in dtc_json:
        if d[0] != '' and d[1] != '':
            dtc = EJ.try_to_value('0x{:0>4s}{:0>2s}'.format(d[0], d[1]))
            DTCs[dtc] = (d[2],d[3])
    Faults = {}
    for f in fault_json:
        event_id = EJ.try_to_value(f[3])
        if f[5] != '' and f[6] !='':
            dtc = EJ.try_to_value('0x{:0>4s}{:0>2s}'.format(f[5], f[6]))
            Faults[event_id] = (dtc, f[0], f[20])
    return DTCs, Faults

class CmdUds(PyUds.BaseDiagnostic):

    def __getattribute__(self, name):
        attr = super(CmdUds, self).__getattribute__(name)
        if name in Uds_Req_List:
            return __class__.Cmd_Print(self, attr)
        else:
            return attr

    def Cmd_Print(self, func):
        def caller(*args, **kwargs):
            cprint("Request : %s" % (func.__name__))
            if 'IsCheck' in kwargs:
                IsCheck = kwargs['IsCheck']
                del kwargs['IsCheck']
            else:
                IsCheck = False
            resp = func(*args, **kwargs)
            if(func.__name__ == 'diagFuncRequest'):
                req_addr = __class__._get_func_addr_str(self)
            else:
                req_addr = __class__._get_request_addr_str(self)
            resp_addr = __class__._get_response_addr_str(self)
            req_value = super(CmdUds, self).__str__()
            resp_value = str(resp)
            cprint("%s:%s" % (req_addr, req_value))
            if resp is None:
                color = 'red'
            elif resp.IsPositiveResponse:
                color = 'green'
            else:
                color = 'red'
            cprint("%s:%s" % (resp_addr, resp_value), fg=color, attrs='bold')
            if IsCheck:
                __class__._resp_process(self, resp)
            return resp
        return caller

    def _get_request_addr_str(self):
        name = super(CmdUds, self).getTpName()
        addr = super(CmdUds, self).getTpAddrInfo()[0]
        if name in ['CanTp', 'CanFdTp']:
            ext = ''
            if addr > 0x7FF:
                ext = 'x'
            return '%03X' % (addr&0x1FFFFFFF) + ext
        elif name == 'FrTp':
            return '%04X' % (addr)
        else:
            return str(addr)

    def _get_func_addr_str(self):
        name = super(CmdUds, self).getTpName()
        addr = super(CmdUds, self).getTpAddrInfo()[1]
        if name in ['CanTp', 'CanFdTp']:
            ext = ''
            if addr > 0x7FF:
                ext = 'x'
            return '%03X' % (addr&0x1FFFFFFF) + ext
        elif name == 'FrTp':
            return '%04X' % (addr)
        else:
            return str(addr)

    def _get_response_addr_str(self):
        name = super(CmdUds, self).getTpName()
        addr = super(CmdUds, self).getTpAddrInfo()[2]
        if name in ['CanTp', 'CanFdTp']:
            ext = ''
            if addr > 0x7FF:
                ext = 'x'
            return '%03X' % (addr&0x1FFFFFFF) + ext
        elif name == 'FrTp':
            return '%04X' % (addr)
        else:
            return str(addr)

    def _resp_process(self, diag_resp):
        if diag_resp is None:
            raise UdsResponseError(color.format(
                'Diag Request not response', fg='red', attrs='bold'))
        elif not diag_resp.IsPositiveResponse:
            raise UdsResponseError(color.format(
                'Diag Request negative response[%02X]' % (diag_resp.NRC), fg='red', attrs='bold'))

class GacUdsCom(object):

    def __init__(self,diag,diag_internal, keygen=None):
        self.diag_internal = diag_internal
        self.diag = diag
        #self.diag_internal = PyUds.BaseDiagnostic(None,None)
        self.keygen = keygen

    def GetSecurityKey(self, seed_level, seed):
        if self.keygen is not None:
            return self.keygen(seed_level, seed)[:len(seed)]
        else:
            return seed

    def CRC32(self, data_array):
        crc32 = 0xffffffff
        for data in data_array:
            crc32 ^= data & 0x000000ff
            for i in range(8):
                if crc32 & 1 != 0:
                    crc32 = (crc32 >> 1) ^ 0xedb88320
                else:
                    crc32 = crc32 >> 1
        crc32 ^= 0xffffffff
        return crc32.to_bytes(4, byteorder='big')

    def UdsUnlock(self, level, diag=None):
        if diag is None:
            diag = self.diag
        resp = diag.SecurityAccess(level, IsCheck=True)
        if resp.DataRecord != [0x00]*(len(resp.DataRecord)):
            key = self.GetSecurityKey(level, resp.DataRecord)
            resp = diag.SecurityAccess(level + 1, *key, IsCheck=True)
        return resp

    def ChangePhase(self, phase):
        phase = int(phase)
        self.diag_internal.SessionControl(0x03, IsCheck=True)
        self.UdsUnlock(0x61,diag=self.diag_internal)
        self.diag_internal.RoutineControl(0x01, 0xF106, phase, IsCheck=True)
        self.diag_internal.RoutineControl(0x03, 0xF106, IsCheck=True)
        self.diag_internal.diagDelay(0.1)
        self.diag_internal.ReadDataByIdentifier(0xFD73, IsCheck=True)
        print('Phase of life update Success!')
    
    def InternalFaultUnPack(self, DataRecord):
        event_list=[]
        for i in range(0, len(DataRecord), 3):
            event_id = (DataRecord[i] << 8) + DataRecord[i + 1]
            status = DataRecord[i + 2]
            if event_id != 0 and status != 0:
                event_list.append((event_id, status))
        return event_list
    
    def DTCUnpack(self, DataRecord):
        dtc_list = []
        for i in range(0, len(DataRecord), 4):
            dtc = (DataRecord[i] << 16) + (DataRecord[i + 1]<<8) + DataRecord[i + 2]
            status = DataRecord[i + 3]
            dtc_list.append((dtc, status))
        return dtc_list
        
    def ReadDTCs(self, status='89'):
        status=status.lower()
        if not status.startswith('0x'):
            status = '0x' + status
        status = int(status, 16)
        resp = self.diag.ReadDtcInformation(0x02, status, IsCheck=True)
        dtc_list = self.DTCUnpack(resp.DataRecord[1:])
        self.DTCPrint(dtc_list)
        
    def DTCPrint(self, dtc_list):
        dtc_info = dtc_fault_config[0]
        print_list = []
        HeaderFmt = "{:<8s}|{:<12s}|{:<32s}|{:<12s}|{:<4s}"
        BodyFmt = "{:^8d}|{:0>6X}      |{:<32s}|{:<12s}|{:0>2X}  "
        col_name = ('No.', "DTC", "DTC Name", "Status", "Hex Status")
        col_ctl = dict(fg=None, bg='yellow', attrs=None)
        for n, dtc in enumerate(dtc_list, start=1):
            d_info = dtc_info.get(dtc[0], ('unknown', 'unknown'))
            status = DTC_STATUS.get(dtc[1] & 0x09, UNKNOWN_STATUS)
            ctl = dict(zip(('fg','bg','attrs'),status[1:]))
            text = (n, dtc[0], d_info[0], status[0], dtc[1])
            print_list.append(dict(ctl=ctl,text=text))
        cprint(HeaderFmt.format(*col_name), **col_ctl)
        #cprint('_'*78)
        for t in print_list:
            cprint(BodyFmt.format(*t['text']), **t['ctl'])

    def ReadInternalFaults(self):
        resp = self.diag_internal.ReadDataByIdentifier(0xFD39, IsCheck=True)
        event_list = self.InternalFaultUnPack(resp.DataRecord)
        self.InternalFaultPrint(event_list)

    def InternalFaultPrint(self, event_list):
        fault_info = dtc_fault_config[1]
        print_list = []
        HeaderFmt = "{:<8s}|{:<12s}|{:<12s}|{:<32s}|{:<12s}|{:<4s}"
        BodyFmt = "{:^8d}|{:<12d}|{:0>6X}      |{:<32s}|{:<12s}|{:0>2X}  "
        col_name = ('No.', "EventID", "DTC", "Event Name", "Status", "Hex Status")
        col_ctl = dict(fg=None, bg='yellow', attrs=None)
        for n, event in enumerate(event_list, start=1):
            e_info = fault_info.get(event[0], (0xFFFFFF, 'unknown','unknown'))
            status = DTC_STATUS.get(event[1] & 0x09, UNKNOWN_STATUS)
            ctl = dict(zip(('fg','bg','attrs'),status[1:]))
            text = (n, event[0], e_info[0], e_info[1], status[0], event[1])
            print_list.append(dict(ctl=ctl,text=text))
        cprint(HeaderFmt.format(*col_name), **col_ctl)
        #cprint('_'*90)
        for t in print_list:
            cprint(BodyFmt.format(*t['text']), **t['ctl'])

    def DownLoad(self, addr, length, buf):
        self.diag.RequestDownload(0x00, 0x44, addr, length, IsCheck=True)
        counter = 0
        for i in range(0, length, 3840):
            counter += 1
            s_buf = buf[i:i+3840]
            self.diag.TransferData(counter, *s_buf, IsCheck=True)
        self.diag.RequestTransferExit(IsCheck=True)        

    def StartEraseMemory(self, addr, length, _format=0x44):
        addr_buf = addr.to_bytes(4, 'big')
        len_buf = length.to_bytes(4, 'big')
        self.diag.RoutineControl(0x01, 0xFF00, _format, *addr_buf, *len_buf, IsCheck=True)
    
    def StartCheckCRC(self, crc):
        if type(crc) is int:
            crc = crc.to_bytes(4, 'big')
        self.diag.RoutineControl(0x01, 0x0202, *crc, IsCheck=True)


    def DownLoadFlashDriver(self, bin_file=None):
        if bin_file is None:
            addr = 0x70100000
            length = 0x0600
            buf = flash_driver
        else:
            with open(bin_file, 'rb') as f:
                bin_buf = f.read()
            addr = int.from_bytes(bin_buf[1:5], 'big')
            length = int.from_bytes(bin_buf[5:9], 'big')
            buf = bin_buf[9:]
        crc = self.CRC32(buf)
        #crc = 0x727F1F65
        self.DownLoad(addr, length, buf)
        self.StartCheckCRC(crc)

    def ClearIP(self):
        self.diag.SessionControl(0x03, IsCheck=True)
        self.diag.SessionControl(0x02, IsCheck=True)
        self.UdsUnlock(0x11)
        self.diag.WriteDataByIdentifier(0xF184, 0xFF, 0x00, 0x01, 0x01, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, IsCheck=True)
        self.diag.RoutineControl(0x01, 0xFF01, IsCheck=True)
        self.DownLoadFlashDriver()
        self.StartEraseMemory(0x80020000, 0x00008000)
        self.diag.ECUReset(0x01, IsCheck=True)
        print('Clear Ip finshed!')
    
    def EOL(self):
        # try:
        #     self.ChangePhase(0x01)
        # except:
        #     print('Can not Change to phase 1')
        # self.diag.diagDelay(0.1)
        # self.ChangePhase(0x01)
        # self.diag.diagDelay(2)
        # self.ChangePhase(0x02)
        # self.diag.diagDelay(2)
        # self.ClearIP()
        # self.diag.diagDelay(1)
        self.diag.SessionControl(0x03, IsCheck=True)
        self.UdsUnlock(0x01)
        self.diag.WriteDataByIdentifier(0x0100, *car_config, IsCheck=True)
        self.diag.WriteDataByIdentifier(0x0101, *can_node_config, IsCheck=True)
        self.diag.WriteDataByIdentifier(0x0202, 0x00, IsCheck=True)
        # self.diag.diagDelay(0.1)
        # self.diag.ECUReset(0x01, IsCheck=True)
        print('All EOL Configuration Success!')

    def UdsCycleRead(self, did):
        pass

    def ParseBinInfo(self, bin):
        h_info = {}
        h_info['DCID'] = bin[:3]
        h_info['SWV'] = bin[3:8]
        h_info['PN'] = bin[8:16]
        h_info['AWV'] = bin[16:0x1B]
        h_info['HeaderVersion'] = bin[0x1B]
        h_info['CRC'] = bin[0x1C:0x20]
        h_info['NOAR'] = bin[0x20]
        h_info['SegMents'] = []
        for i in range(h_info['NOAR']):
            addr = int.from_bytes(bin[0x21 + i * 4:0x25 + i * 4], byteorder='big')
            length = int.from_bytes(
                bin[0x25 + i * 4:0x29 + i * 4], byteorder='big')
            h_info['SegMents'].append(dict(addr=addr, length=length))
        start = 0x21 + 8 * len(h_info['SegMents'])
        crc32 = self.CRC32(bin[start:])
        if crc32 != h_info['CRC']:
            raise Exception('Bin File CRC Error!')
        for h in h_info['SegMents']:
            end = start + h['length']
            h['buf'] = bin[start:end]
            start = end
        return h_info

    def BootDownLoad(self, *files):
        self.diag.SessionControl(0x03, IsCheck=True)
        self.diag.SessionControl(0x02, IsCheck=True)
        self.UdsUnlock(0x11)
        d = datetime.now()
        fig_buf = [0x01,d.year-2000,d.month,d.day] + list(b'PyUds0')
        self.diag.WriteDataByIdentifier(0xF184, *fig_buf, IsCheck=True)
        for file in files:
            with open(file, 'rb') as f:
                bin_s = f.read()
            b_info = self.ParseBinInfo(bin_s)
            self.DownLoadFlashDriver()
            erase_addr = b_info['SegMents'][0]['addr']
            erase_len = sum([seg['length'] for seg in b_info['SegMents']])
            self.StartEraseMemory(erase_addr, erase_len)
            for seg in b_info['SegMents']:
                self.DownLoad(seg['addr'], seg['length'], seg['buf'])
            self.StartCheckCRC(b_info['CRC'])
        self.diag.RoutineControl(0x01, 0xFF01, IsCheck=True)
        self.diag.ECUReset(0x01, IsCheck=True)
        print('Bootload download files success!')

    def GacUds(self):
        print('Please input request diagnostic cmd or exit:')
        self._uds_cmd_process(self.diag)

    def GacClearDTC(self):
        self.diag.ClearDiagnosticInformation(0xFFFFFF, IsCheck=True)

    def GacInternalUds(self):
        print('Please input request diagnostic cmd or exit:')
        self._uds_cmd_process(self.diag_internal)
    
    def _uds_cmd_process(self, diag):
        while 1:
            cmds = input()
            if cmds in ('exit', 'quit'):
                diag.StopTesterPresent()
                return
            elif cmds == 'start':
                diag.StartTesterPresent()
                print('Start Send TesterPresent')
            elif cmds == 'stop':
                diag.StopTesterPresent()
                print('Stop Send TesterPresent')
            elif cmds.startswith('unlock'):
                ls = cmds.split()
                if len(ls) < 2:
                    print('please input the unlock level:')
                else:
                    level = int('0x'+ls[1], 16)
                    self.UdsUnlock(level, diag=diag)
            else:
                for cmd in self._get_cmd_list(cmds):
                    diag.diagRawRequest(*cmd)


    def _get_cmd_list(self, cmd):
        cmd_list = []
        parten = r"[^;0-9A-Fa-f\s]"
        result = re.search(parten, cmd)
        if result is not None:
            print('print unknown cmd or position %d, [%s] is not a hex value'%(result.start(), cmd[result.start()]))
            return []
        l1 = cmd.split(';')
        for l in l1:
            parten = r"[0-9A-Fa-f]{1,2}"
            result = re.findall(parten, l)
            hex_list = [int('0x' + x, 16) for x in result]
            cmd_list.append(hex_list)
        return cmd_list

def main(args):
    global dtc_fault_config
    config = Scripts.UdsConfigParse('UdsConfig.json')
    dtc_config_path = config.config['DTC'][0]['Path']
    dtc_fault_config = DTCFaultConfigLoad(dtc_config_path)
    bus = config.GetBus('CanBus1')
    # diag = CmdUds(uds_client=config.GetUdsClient('CanPhy'))
    # diag_internal = CmdUds(uds_client=config.GetUdsClient('CanInternal'))
    diag = config.GetUdsDiag('CanPhy', diag_cls='CmdUds')
    diag_internal = config.GetUdsDiag('CanInternal', diag_cls='CmdUds')
    key_gen = config.GetKeyGens("GAC_A39")
    uds = GacUdsCom(diag, diag_internal, key_gen)
    Cmds = {
        "eol": uds.EOL,
        "clearip": uds.ClearIP,
        "cleardtc": uds.GacClearDTC,
        "phase": uds.ChangePhase,
        "boot": uds.BootDownLoad,
        'uds': uds.GacUds,
        'internal': uds.GacInternalUds,
        'dtc': uds.ReadDTCs,
        'fault':uds.ReadInternalFaults
    }
    with PyUds.ThreadSafety(bus):
        try:
            Cmds[args[0]](*args[1:])
        except UdsResponseError as ex:
            print(ex)
        except KeyError as ex:
            print(ex)
            print('Please input cmd in:', Cmds.keys())
        except TypeError as ex:
            print(ex)
            desc = '~~~~~~~~~~~~~~example~~~~~~~~~~~~~\n'
            desc += '  eol: gac eol configure\n'
            desc += '  clearip: clear ip fixedcal an alog3 fixedcal\n'
            desc += '  phase n: update to phase of life to 0,1,2\n'
            desc += '  boot "file1" "file2" ...: download files\n'
            desc += '  dtc [stauts]: read dtc information by stauts \n'
            desc += '  fault: read internal faults\n'
            desc += '  uds: enter diagnostic mode\n'
            desc += '  internal: enter internal diagnostic mode\n'
            print(desc)

def argv_process(args):
    cmds = args[:1]
    if args[0] == 'boot':
        for file in args[1:]:
            pfile = os.path.abspath(file)
            cmds.append(pfile)
    else:
        cmds = args[:]
    return cmds


if __name__ == '__main__':
    if len(sys.argv) > 1:
        cmds = argv_process(sys.argv[1:])
        wk_path = os.path.join(os.path.dirname(__file__), 'gac_scripts')
        os.chdir(wk_path)
        main(cmds)
    else:
        desc = 'please used with following args:\n'
        desc += '  eol: gac eol configure\n'
        desc += '  clear: clear ip fixedcal an alog3 fixedcal\n'
        desc += '  phase n: update to phase of life to 0,1,2\n'
        desc += '  boot "file1" "file2" ...: download files\n'
        desc += '  dtc [stauts]: read dtc information by stauts \n'
        desc += '  fault: read internal faults\n'
        desc += '  uds: enter diagnostic mode\n'
        desc += '  internal: enter internal diagnostic mode\n'
        print(desc)
    pass
