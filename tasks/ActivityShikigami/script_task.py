# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
import random
from datetime import datetime, timedelta, time

from tasks.base_task import BaseTask
from tasks.Component.GeneralBattle.general_battle import GeneralBattle
from tasks.AreaBoss.assets import AreaBossAssets
from tasks.Component.BaseActivity.base_activity import BaseActivity
from tasks.Component.BaseActivity.config_activity import ApMode
from tasks.ActivityShikigami.assets import ActivityShikigamiAssets
from module.logger import logger
from module.exception import TaskEnd


class ScriptTask(BaseActivity, ActivityShikigamiAssets):

    def is_ticket(self) -> bool:
        # 判断是否还有挑战次数
        self.screenshot()
        cu, res, total = self.O_NUMBER.ocr(self.device.image)
        if res == 0 and total != 0:
            logger.info("没有挑战次数了")
            return False
        logger.info("剩余挑战次数:"+str(res)+"次")
        return True


    def run(self) -> None:

        config = self.config.activity_shikigami
        self.limit_time: timedelta = config.general_climb.limit_time
        if isinstance(self.limit_time, time):
            self.limit_time = timedelta(hours=self.limit_time.hour, minutes=self.limit_time.minute,
                                        seconds=self.limit_time.second)
        self.limit_count = config.general_climb.limit_count


        # 流程应该是 在页面处：
        # 1. 判定计数是否超了，时间是否超了
        # 2. 如果是消耗活动体力，判定活动体力是否足够 如果是消耗一般的体力，判定一般体力是否足够
        # 3. 如果开启买体力，就买体力
        # 4. 如果开启了切换到游戏体力，就切换
        while 1:
            # 1
            if self.limit_time is not None and self.limit_time + self.start_time < datetime.now():
                logger.info("Time out")
                break
            if self.current_count >= self.limit_count:
                logger.info("Count out")
                break
            # 2
            self.wait_until_appear(self.I_FIRE)
            # 判断是否还有挑战次数
            if not self.is_ticket():
                break
            # 点击战斗

            logger.info("Click battle")
            while 1:
                self.screenshot()
                if self.appear_then_click(self.I_FIRE, interval=1):
                    continue
                if not self.appear(self.I_FIRE):
                    break

            if self.run_general_battle(config=config.general_battle):
                logger.info("General battle success")

        self.set_next_run(task="ActivityShikigami", success=True)
        raise TaskEnd






if __name__ == '__main__':
    from module.config.config import Config
    from module.device.device import Device
    from memory_profiler import profile
    c = Config('oas1')
    d = Device(c)
    t = ScriptTask(c, d)

    t.run()