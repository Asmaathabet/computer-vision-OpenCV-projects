import pywhatkit

pywhatkit.sendwhatmsg_instantly(
    phone_no="+32465318161",
    message="Hello! Happy Birthday! Wishing you a wonderful day filled with joy and surprises.",
    wait_time=13,       # Time to wait before sending the message
    # tab_close=True,     # Close the browser tab after sending the message
    close_time=26        # Time to wait before closing the tab   
)
