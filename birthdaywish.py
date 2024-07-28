import pandas as pd 
import datetime
import smtplib 
 
GMAIL_ID = ''
GMAIL_PASS = '' 

def sendEmail(to, sub, msg ):
    print(f"eamil to {to} with subject {sub} and message {msg} sent")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.starttls(GMAIL_ID, GMAIL_PASS)
    s.send(GMAIL_ID, to, f"subject: {sub} and message: {msg")

if __name__  == "__main__":
     df= pd.read_excel("wish.xlsx")
     #print(df)
     #today date is this 
     today=datetime.datetime.now().strftime("%d-%m") 
     YearNow=datetime.datetime.now().strftime("%y")                           
                          
    #  print(type(today))
     writeInd=[]
     
    
     for index,item in df.iterrows():
       # print(index,item['Birthday'])
        bdy =item['Birthday'].strftime("%d-%m")
        print(bdy)
        if(today==bdy)and YearNow not in str(item['year']):
            
            sendEmail(item['Email'], "happy bdy", item['Dialogue'])
            writeInd.append(index)
            
           
            #print(writeInd)
        for i in writeInd:
          yr = df.loc[i, 'year']
          df.loc[i, 'year'] = str(yr) + ', ' + str(YearNow)
        #   print(df.loc[i, 'year'])  
        # print(df)  
          df.to_excel('wish.xlsx')  
     
  