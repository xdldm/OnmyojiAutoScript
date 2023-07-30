from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class EvoZoneAssets: 


	# Image Rule Assets
	# 火麒麟进入 
	I_FIRE_KIRIN = RuleImage(roi_front=(84,126,217,406), roi_back=(84,126,217,406), threshold=0.8, method="Template matching", file="./tasks/EvoZone/o/o_fire_kirin.png")
	# 组队 
	I_FORM_TEAM = RuleImage(roi_front=(937,591,100,100), roi_back=(937,591,100,100), threshold=0.8, method="Template matching", file="./tasks/EvoZone/o/o_form_team.png")
	# description 
	I_EVOZONE_LOCK = RuleImage(roi_front=(573,559,31,32), roi_back=(548,554,65,54), threshold=0.8, method="Template matching", file="./tasks/EvoZone/o/o_evozone_lock.png")
	# description 
	I_EVOZONE_UNLOCK = RuleImage(roi_front=(575,558,26,29), roi_back=(560,553,56,40), threshold=0.8, method="Template matching", file="./tasks/EvoZone/o/o_evozone_unlock.png")
	# 点击挑战 
	I_EVOZONE_FIRE = RuleImage(roi_front=(1095,577,131,124), roi_back=(1095,577,131,124), threshold=0.6, method="Template matching", file="./tasks/EvoZone/o/o_evozone_fire.png")
	# 式神录 
	I_SHI_RECORDS = RuleImage(roi_front=(821,638,48,45), roi_back=(821,638,48,45), threshold=0.8, method="Template matching", file="./tasks/EvoZone/o/o_shi_records.png")
	# description 
	I_EVOZONE_MATCHING = RuleImage(roi_front=(62,568,44,114), roi_back=(62,568,44,114), threshold=0.8, method="Template matching", file="./tasks/EvoZone/o/o_evozone_matching.png")
	# 小小宠物，发现宝藏 
	I_PET_PRESENT = RuleImage(roi_front=(873,184,62,147), roi_back=(873,184,62,147), threshold=0.8, method="Template matching", file="./tasks/EvoZone/o/o_pet_present.png")
	# 风麒麟进入 
	I_WIND_KIRIN = RuleImage(roi_front=(377,126,232,420), roi_back=(377,126,232,420), threshold=0.8, method="Template matching", file="./tasks/EvoZone/o/o_wind_kirin.png")
	# 水麒麟进入 
	I_WATER_KIRIN = RuleImage(roi_front=(671,122,236,420), roi_back=(671,122,236,420), threshold=0.8, method="Template matching", file="./tasks/EvoZone/o/o_water_kirin.png")
	# 雷麒麟进入 
	I_LIGHTNING_KIRIN = RuleImage(roi_front=(967,121,239,419), roi_back=(967,121,239,419), threshold=0.8, method="Template matching", file="./tasks/EvoZone/o/o_lightning_kirin.png")


	# List Rule Assets
	# 这个是觉醒界面选择不同层数的 
	L_LAYER_LIST = RuleList(folder="./tasks/EvoZone/res", direction="vertical", mode="ocr", roi_back=(138,130,359,500), size=(44, 88), 
					 array=["壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖", "拾"])


	# Ocr Rule Assets
	# Ocr-description 
	O_O_TEST_OCR = RuleOcr(roi=(126,136,360,491), area=(126,136,360,491), mode="Full", method="Default", keyword="", name="o_test_ocr")


