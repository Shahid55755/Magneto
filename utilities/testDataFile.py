from selenium import webdriver
from selenium.webdriver.common.by import By


class TestData:
    # Login page locator
    sign_in = (By.XPATH, "(//a[contains(text(),'Sign In')])[1]")
    login_email = (By.CSS_SELECTOR, "#email")
    login_password = (By.CSS_SELECTOR, "input[title='Password'][class='input-text']")
    login_Add = (By.XPATH, "(//span[contains(text(),'Sign In')])[1]")
    verify = (By.CSS_SELECTOR, "div[class='panel header'] span[class='logged-in']")

    # Create account locators
    create_new_account = (By.CSS_SELECTOR, "header[class='page-header'] li:nth-child(3) a:nth-child(1)")
    firstname = (By.CSS_SELECTOR, "#firstname")
    lastname = (By.ID, "lastname")
    email = (By.XPATH, "//input[@id='email_address']")
    password = (By.CSS_SELECTOR, "#password")
    Confirm = (By.CSS_SELECTOR, "#password-confirmation")
    Add = (By.CSS_SELECTOR, "button[title='Create an Account'] span")
    success = (By.XPATH, "//div[@class='message-success success message']")
    duplicate_account = (By.CSS_SELECTOR, "img[alt='Radiant Tee']")
    duplicate_account1 = (By.CSS_SELECTOR, "div[data-bind='html: $parent.prepareMessageForHtml(message.text)']")

    # Search Items locators
    search_id = (By.CSS_SELECTOR, "#search")
    select_item = (By.XPATH, "//*[@id='qs-option-4']/span[1]")
    get_items = (By.CSS_SELECTOR, ".product-image-container")
    get_add_to_path = (By.XPATH, "//span[normalize-space()='Add to Cart']")
    verify_text = (By.XPATH, "//*[@id='product-price-1316']/span")
    size = (By.ID, "option-label-size-143-item-166")
    color = (By.ID, "option-label-color-93-item-56")

    pick_first_item = (By.XPATH, "(//div[@class='price-box price-final_price'])[1]")

    # After Add to cart (Click option (Count) for proceed to checkout)
    count = (By.XPATH, "/html/body/div[2]/header/div[2]/div[1]/a/span[2]/span[1]")
    verify_text_success = (By.CSS_SELECTOR, "div[data-bind='html: $parent.prepareMessageForHtml(message.text)']")
    cart_success_message = (By.CSS_SELECTOR, "div[data-bind='html: $parent.prepareMessageForHtml(message.text)']")
    wishlist_success_msg = (By.CSS_SELECTOR, "div[data - bind = 'html: $parent.prepareMessageForHtml(message.text)']")

    # add to wishlist
    add_to_wishlist = (By.CSS_SELECTOR, "div[class='product-addto-links'] a[class='action towishlist']")
    # my product reviews
    review = (By.XPATH, "//a[normalize-space()='My Product Reviews']")
    message_ = (By.CSS_SELECTOR, ".messages")
    Check_reviews = (By.XPATH, "(//span[contains(text(),'Reviews')])[1]")
    verify_text_cus_review = (By.XPATH, "//strong[normalize-space()='Customer Reviews']")

    # ADD Rating
    five_star = (By.ID, ".field.required.review-field-ratings")
    rating_label = (By.ID, "Rating_4_label")
    review_form = (By.ID, "review-form")
    nick_name = (By.ID, "nickname_field")
    summary_field = (By.ID, "summary_field")
    review_field = (By.ID, "review_field")
    submit_button = (By.CSS_SELECTOR, "button[class='action submit primary']")

    # Items to check out
    click_items_count = (By.XPATH, "/html[1]/body[1]/div[2]/header[1]/div[2]/div[1]/a[1]/span[2]")

    # Proceed to checkout
    btn_chk_out = (By.XPATH, "//button[@id='top-cart-btn-checkout']")
    c_email = (By.ID, "customer-email")
    c_email_data = "shahid_ali@yahoo.com"
    c_name = (By.NAME, "firstname")
    c_l_name = (By.NAME, "lastname")
    c_company = (By.NAME, "company")
    c_street = (By.NAME, "street[0]")
    c_street1 = (By.NAME, "street[1]")
    c_street2 = (By.NAME, "street[2]")
    c_city = (By.NAME, "city")
    c_region = By.NAME, "region_id"
    c_postcode = (By.NAME, "postcode")
    c_country = By.NAME, "country_id"
    c_telephone = (By.NAME, "telephone")
    next_button = (By.XPATH, "//button[@class='button action continue primary']//span[text()='Next']")
    p_order_btn = (By.CSS_SELECTOR, "button[title='Place Order']")
    success_order = (By.CSS_SELECTOR, ".base")



