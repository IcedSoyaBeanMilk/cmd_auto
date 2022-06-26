from time import sleep
from mcdreforged.api.all import *
import time
import os
import collections
from typing import List, Optional, Callable, Any, Union, Dict, Mapping

@new_thread
def excuter(server: PluginServerInterface, commands : List[str]):
    for cmd in commands:
        print(cmd)
        server.execute(cmd)
        time.sleep(1)
    return

class Config(Serializable):
    commandsList: dict = {"the_nether": ["player Alex spawn"]}

Prefix = '!!cmdAuto'
config: Config
ConfigFilePath = 'config/cmdAuto.json'

def on_load(server: PluginServerInterface, old):
    global config
    config = server.load_config_simple(file_name=ConfigFilePath, target_class=Config, in_data_folder=False)
    server.register_command(Literal(Prefix).\
        then(
            Literal('help').runs(lambda src: src.reply('不知道写啥，随便打印点东西吧！'))
        ).\
        then(
            Literal('excute').\
                then(
                    Text('commandName').
                    suggests(lambda: config.commandsList.keys()).
                    runs(lambda src, ctx: excuter(server,config.commandsList.get(ctx['commandName'])))
                )
        )
    )