from booking.booking import Booking

# inst=Booking() #booking instance
# inst.landFirstPage()

#sometime we can't run bots like that because when we run it for many times then it will open many browser window hence not a feasible and efficient way to do thing
#for this reason we will colase our program bot after it complete its task

try:
    with Booking() as bot:
        bot.landFirstPage()
        #bot.changeCurrency(currency="USD")
        # bot.selectPlaceToGo(place_to_go=input("Where you want to go?\n"))
        # bot.select_date(check_in_date=input("checkin date(YY/MM/DD:2022-02-28):\n"),check_out_date=input("checkout date:\n")) #"2022-02-28"
        # bot.select_adults(count=input(' how many people'))
        bot.selectPlaceToGo(place_to_go="goa")
        bot.select_date(check_in_date="2022-05-28",check_out_date="2022-06-01")
        bot.select_adults(count=2)
        bot.click_search()
        bot.apply_filterations()
        bot.refresh() # A workaround to let our  bot grab the data properly
        bot.report_results()
except Exception as e:
    if 'in PATH' in str(e):
        print('''                 you are trying to run the bot from command line
                 please add to PATH your selenium Drivers
                 Windows:
                        set Path=%PATH%;C:Path-to-your-folder
                 Linux:
                        PATH=$PATH:/path/toyour/folder
        ''')
    else:
        raise
        
#after executing the above block python gonna call/execute  __exit__() method of Booking class which gonna quit the window(read more about context managers)
#it is not required to write __exit__() again in booking but for practice we had done that

