from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.select_place_to_go("New York")
    bot.select_dates(check_in_date='2023-01-29',
                     check_out_date='2023-02-10')
    bot.select_adults(count=9)
    bot.click_search()