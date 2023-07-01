# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
from datetime import datetime, timedelta
import time

from tasks.base_task import BaseTask
from tasks.Component.GeneralBattle.general_battle import GeneralBattle
from tasks.AreaBoss.assets import AreaBossAssets
from tasks.Component.BaseActivity.base_activity import BaseActivity
from tasks.Component.BaseActivity.config_activity import ApMode
from tasks.ActivityShikigami.assets import ActivityShikigamiAssets
from module.logger import logger
from module.exception import TaskEnd


class ScriptTask(BaseActivity, ActivityShikigamiAssets):

    def run(self) -> None:

        config = self.config.activity_shikigami
        self.limit_time: timedelta = config.general_climb.limit_time
        self.limit_count = config.general_climb.limit_count

        self.home_main()

        # 设定是否锁定阵容
        self.wait_until_appear(self.I_BACK_GREEN)
        if config.general_battle.lock_team_enable:
            logger.info("Lock team")
            while 1:
                self.screenshot()
                if self.appear_then_click(self.I_UNLOCK, interval=1):
                    continue
                if self.appear(self.I_LOCK):
                    break
        else:
            logger.info("Unlock team")
            while 1:
                self.screenshot()
                if self.appear_then_click(self.I_LOCK, interval=1):
                    continue
                if self.appear(self.I_UNLOCK):
                    break

        # 选择是游戏的体力还是活动的体力
        current_ap = config.general_climb.ap_mode
        self.switch(current_ap)

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
            is_remain = self.check_ap_remain(current_ap)
            # 如果没有剩余了且这个时候是体力，就退出活动
            if not is_remain and current_ap == ApMode.AP_GAME:
                logger.info("Game ap out")
                break
            # 如果不是那就切换到体力
            elif not is_remain and current_ap == ApMode.AP_ACTIVITY:
                logger.info("Activity ap out and switch to game ap")
                current_ap = ApMode.AP_GAME
                self.switch(current_ap)


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

        self.main_home()
        self.set_next_run(task="ActivityShikigami", success=True)
        raise TaskEnd


    def home_main(self) -> bool:
        """
        从庭院到活动的爬塔界面
        :return:
        """
        logger.hr("Enter Shikigami", 2)
        while 1:
            self.screenshot()
            if self.appear_then_click(self.I_SHI, interval=1):
                continue
            if self.appear_then_click(self.I_DRUM, interval=1):
                continue
            if self.appear_then_click(self.I_BATTLE, interval=1):
                continue
            if self.appear(self.I_FIRE):
                break


    def main_home(self) -> bool:
        """
        从活动的爬塔界面到庭院
        :return:
        """
        logger.hr("Exit Shikigami", 2)
        while 1:
            self.screenshot()
            if self.appear_then_click(self.I_BACK_GREEN, interval=1):
                continue
            if self.appear(self.I_SHI):
                break

    def check_ap_remain(self, current_ap: ApMode) -> bool:
        """
        检查体力是否足够
        :return: 如何还有体力，返回True，否则返回False
        """
        self.screenshot()
        if current_ap == ApMode.AP_ACTIVITY:
            cu, res, total = self.O_REMAIN_AP_ACTIVITY.ocr(image=self.device.image)
            if cu == 0 and cu + res == total:
                logger.warning("Activity ap not enough")
                return False
            return True

        elif current_ap == ApMode.AP_GAME:
            cu, res, total = self.O_REMAIN_AP.ocr(image=self.device.image)
            if cu == total and cu + res == total:
                logger.warning("Game ap not enough")
                return False
            return True

    def switch(self, current_ap: ApMode) -> None:
        """
        切换体力
        :param current_ap:
        :return:
        """
        if current_ap == ApMode.AP_ACTIVITY:
            logger.info("Select activity ap")
            while 1:
                self.screenshot()
                if self.appear(self.I_AP_ACTIVITY):
                    break
                if self.appear(self.I_AP, interval=1):
                    self.appear_then_click(self.I_SWITCH, interval=2)  # 点击切换
        else:
            logger.info("Select game ap")
            while 1:
                self.screenshot()
                if self.appear(self.I_AP):
                    break
                if self.appear(self.I_AP_ACTIVITY, interval=1):
                    self.appear_then_click(self.I_SWITCH, interval=2)
