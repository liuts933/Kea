import sys
sys.path.append("..")
from kea import *

class Test(KeaTest):
    
    

    @initializer()
    def set_up(self):
        d(text="Get Started").click()

    @mainPath()
    def reschedule_should_display_another_card_mainpath(self):
        d(resourceId="com.ichi2.anki:id/deckpicker_name").click()

    # 5167
    @precondition(
        lambda self: d(resourceId="com.ichi2.anki:id/flashcard").exists() and
        d(resourceId="com.ichi2.anki:id/action_flag").exists() and
        d(resourceId="com.ichi2.anki:id/bottom_area_layout").exists()
    )
    @rule()
    def reschedule_should_display_another_card(self):
        content = d(resourceId="content").child(className="android.view.View").get_text()
        print("content: " + str(content))
        d(description="More options").click()
        
        d(text="Reschedule").click()
        
        d(text="Reschedule for review in x days").click()
        
        d(className="android.widget.EditText").set_text("1")
        
        d(text="OK").click()
        
        new_content = d(resourceId="content").child(className="android.view.View").get_text()
        print("new_content: " + str(new_content))
        assert content != new_content, "should display another card"




if __name__ == "__main__":
    t = Test()
    
    setting = Setting(
        apk_path="./apk/ankidroid/2.18alpha6.apk",
        device_serial="emulator-5554",
        output_dir="output/ankidroid/5167/guided_new/1",
        policy_name="random"
    )
    start_kea(t,setting)
    
