from datetime import datetime
  
current_time = datetime.now()  
str_date = current_time.strftime("%Y_%m_%d_%H_%M_%S")

print(str_date)
