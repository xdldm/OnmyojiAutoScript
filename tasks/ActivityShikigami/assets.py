from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class ActivityShikigamiAssets: 


	# Image Rule Assets
	# 战斗按钮 
	I_FIRE = RuleImage(roi_front=(1120,567,100,100), roi_back=(1120,567,100,100), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_fire.png")
	# description 
	I_ = RuleImage(roi_front=(1118,568,100,100), roi_back=(1118,568,100,100), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_.png")


	# Ocr Rule Assets
	# 挑战次数 
	O_NUMBER = RuleOcr(roi=(1183.2,671.8000000000001,75.20000000000005,30), area=(1118.4,570.4000000000001,100,100), mode="DigitCounter", method="Default", keyword="", name="number")


