# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from pydantic import BaseModel, Field

from tasks.Component.GeneralBattle.config_general_battle import GeneralBattleConfig
from tasks.Component.config_scheduler import Scheduler
from tasks.Component.config_base import ConfigBase, TimeDelta
from tasks.Component.BaseActivity.config_activity import GeneralClimb

class CommonActivityShikigami(ConfigBase):
    scheduler: Scheduler = Field(default_factory=Scheduler)
    general_climb: GeneralClimb = Field(default_factory=GeneralClimb)
    general_battle: GeneralBattleConfig = Field(default_factory=GeneralBattleConfig)




