#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################


page_title = "xpath,//h2"
temperature_field = "xpath,//span[@id ='temperature']"
click_moisturizers = "xpath,//button[text()='Buy moisturiers']" 
click_sunscreens= "xpath,//button[text()=='Buy sunscreens']"
heading_text = "xpath,//h2[contains(text(),'%s')]"
heading_sunscreen = "xpath,//h2[contains(text(),'Sunscreens')]"
heading_moisturizer = "xpath,//h2[contains(text(),'Moisturizers')]"

add_moisturizer_sunscreen_button =""  
cart_count ="xpath,//span[contains(text(),'item(s)')]"

cart_button ="xpath,//button[@class='thin text-nav-ink']" 
pay_with_card ="xpath,//button[@type='submit']"

price_tag ="xpath,//div[contains(@class,'col-4')]"
add_item ="xpath,//p[contains(text(),'%s')]/following-sibling::button[@class='btn btn-primary']"

almond_price ="xpath,//*[contains(text(),'almond') or contains(text(),'Almond')]/following-sibling::p"
aloe_price ="xpath,//*[contains(text(),'aloe') or contains(text(),'Aloe')]/following-sibling::p"

spf50_price ="xpath,//*[contains(text(),'spf-50') or contains(text(),'SPF-50')]/following-sibling::p"
spf30_price ="xpath,//*[contains(text(),'spf-30') or contains(text(),'SPF-30')]/following-sibling::p"